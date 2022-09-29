import argparse
import os
from datetime import datetime

import requests
from dotenv import load_dotenv

import download_space_image


def fetch_nasa_json(token):
    params = {"api_key": token}
    response = requests.get(
        "https://api.nasa.gov/EPIC/api/natural/images", params=params
    )
    response.raise_for_status()
    return response.json()


def fetch_nasa_urls(token, photos_number, json):
    urls = []
    for number in range(photos_number):
        name = json[number]["image"]
        time = datetime.fromisoformat(json[number]["date"])
        params = {"api_key": token}
        response = requests.get(
            f"https://api.nasa.gov/EPIC/archive/natural/{time:%Y}/{time:%m}/{time:%d}/png/{name}.png",
            params=params
        )
        response.raise_for_status()
        urls.append(response.url)
    return urls


def download_images(urls):
    for number, epic in enumerate(urls):
        filename = os.path.join("images", f"nasa_epic_{number}.png")
        download_space_image.download_image(epic, filename)


if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser(
        description="Выгружает картинки NASA EPIC."
    )
    parser.add_argument(
        "-d",
        dest="photos_number",
        help="Количество скачиваемых фотографий NASA EPIC.",
        default="5",
        type=int,
    )
    get_photos_number = lambda: parser.parse_args().photos_number
    json = fetch_nasa_json(os.environ["NASA_TOKEN"])
    urls = fetch_nasa_urls(os.environ["NASA_TOKEN"], get_photos_number(), json)
    download_images(urls)
