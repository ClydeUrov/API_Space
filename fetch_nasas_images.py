import os
import requests
from pathlib import Path
from os.path import splitext
import urllib.parse
from dotenv import load_dotenv


def download_image(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def image_expansion(url):
    url_parts = urllib.parse.urlparse(url)
    extracted_link = f'{url_parts.path}'
    s = splitext(extracted_link)
    return s[1]


def fetch_nasas_images(token):
    params = {'api_key': token, 'start_date': '2022-08-01'}
    response = requests.get(
        'https://api.nasa.gov/planetary/apod',
         params=params
    )
    response.raise_for_status()
    nasa_images = response.json()
    for nasa_apod_number, image in enumerate(nasa_images):
        format_url = image_expansion(image['url'])
        filename = f'images/nasa_apod_{nasa_apod_number}{format_url}'
        download_image(image['url'], filename) 


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.getenv("NASA_TOKEN")
    Path("images").mkdir(parents=True, exist_ok=True)
    fetch_nasas_images(nasa_token)