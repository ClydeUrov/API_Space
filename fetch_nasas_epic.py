import os
import requests
from dotenv import load_dotenv
from datetime import datetime
import download_space_image
import argparse


def fetch_nasa_epic(token, photos_number):
    params = {'api_key': token}
    epic_response = requests.get(
        'https://api.nasa.gov/EPIC/api/natural/images',
        params=params
    )
    epics_url = []
    for number in range(0, photos_number):
        epic_name = epic_response.json()[number]['image']
        epic_time = datetime.fromisoformat(epic_response.json()[number]['date'])
        response = requests.get(
            f'https://api.nasa.gov/EPIC/archive/natural/{epic_time:%Y}/{epic_time:%m}/{epic_time:%d}/png/{epic_name}.png',
            params=params
        )
        response.raise_for_status()
        epics_url.append(response.url)
    for nasa_epic_number, epic in enumerate(epics_url):
        filename = os.path.join('images', f'nasa_epic_{nasa_epic_number}.png')
        download_space_image.download_image(epic, filename)


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser(description="Выгружает картинки NASA EPIC.")
    parser.add_argument(
        '-d',
        dest='photos_number',
        help='Количество скачиваемых фотографий NASA EPIC.',
        default='5',
        type=int
    )
    parser.add_argument(
        '-t',
        dest='nasa_token',
        help='NASA Токен',
        default=os.environ['NASA_TOKEN']
    )
    get_photos_number = lambda: parser.parse_args().photos_number
    get_nasa_token = lambda: parser.parse_args().nasa_token
    fetch_nasa_epic(get_nasa_token(), get_photos_number())
