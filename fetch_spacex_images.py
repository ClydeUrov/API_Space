import os
import requests
from pathlib import Path
import download_space_image
import argparse


def fetch_spacex_last_launch():
    response = requests.get(
        f'https://api.spacexdata.com/v5/launches/{args.launch_id}'
    )
    if not response.json()['links']['flickr']['original']: response = requests.get(
        'https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384'
    ) 
    response.raise_for_status()
    spacex_links = (response.json()['links']['flickr']['original'])
    for spacex_number, spacex in enumerate(spacex_links):
        filename = os.path.join('images', f'spacex_{spacex_number}.jpg')
        download_space_image.download_image(spacex, filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Выгружает картинки SpaceX"
    )
    parser.add_argument(
        '-d',
        dest='launch_id',
        help='ID запуска SpaceX',
        default='latest'
    )
    args = parser.parse_args()
    Path("images").mkdir(parents=True, exist_ok=True)
    fetch_spacex_last_launch()
