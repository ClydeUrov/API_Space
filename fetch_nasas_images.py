import os
import requests
import urllib.parse
from os.path import splitext
from dotenv import load_dotenv
from datetime import datetime
import download_space_image
import argparse


def image_expansion(url):
    url_parts = urllib.parse.urlparse(url)
    extracted_link = url_parts.path
    return splitext(extracted_link)[1]


def fetch_nasas_images(token):
    params = {'api_key': token, 'start_date': date_time.date()}
    response = requests.get(
        'https://api.nasa.gov/planetary/apod',
        params=params
    )
    response.raise_for_status()
    images_url = [part['url'] for part in response.json() if part['media_type'] == 'image']
    for nasa_apod_number, image in enumerate(images_url):
        filename = os.path.join(
            "images", f"nasa_apod_{nasa_apod_number}{image_expansion(image)}"
        )
        download_space_image.download_image(image, filename)


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser(
        description="Выгружает картинки NASA APOD"
    )
    parser.add_argument(
        '-d',
        dest='date_time',
        help='Дата начала выгрузки картинок. [year]-[month]-[day]',
        default='22-08-28'
    )
    nasa_token = os.environ['NASA_TOKEN']
    date_time = datetime.strptime(parser.parse_args().date_time, "%y-%m-%d")
    fetch_nasas_images(nasa_token)
