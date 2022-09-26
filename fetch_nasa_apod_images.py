import argparse
import os
import urllib.parse
from datetime import datetime
from os.path import splitext

import requests
from dotenv import load_dotenv

import download_space_image


def assign_extension(url):
    url_parts = urllib.parse.urlparse(url)
    extracted_link = url_parts.path
    return splitext(extracted_link)[1]


def fetch_nasa_images(token):
    params = {"api_key": token, "start_date": date_time.date()}
    response = requests.get(
        "https://api.nasa.gov/planetary/apod",
        params=params
    )
    response.raise_for_status()
    urls = [part["url"] for part in response.json() if part["media_type"] == "image"]
    for number, image in enumerate(urls):
        filename = os.path.join(
            "images", f"nasa_apod_{number}{assign_extension(image)}"
        )
        download_space_image.download_image(image, filename)


if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser(
        description="Выгружает картинки NASA APOD"
    )
    parser.add_argument(
        "-d",
        dest="date_time",
        help="Дата начала выгрузки картинок. [year]-[month]-[day]",
        default="22-08-28",
    )
    date_time = datetime.strptime(parser.parse_args().date_time, "%y-%m-%d")
    fetch_nasa_images(os.environ["NASA_TOKEN"])
