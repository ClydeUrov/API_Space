import os
import requests
from dotenv import load_dotenv
from datetime import datetime
import download_space_image
import argparse
    

def fetch_nasa_json(token):
    params = {'api_key': token}
    response = requests.get(
        'https://api.nasa.gov/EPIC/api/natural/images',
        params=params
    )
    response.raise_for_status()
    return response.json()


def fetch_nasa_url(token, photos_number, nasa_json):
    epics_url = []
    for number in range(photos_number):
        epic_name = nasa_json[number]['image']
        epic_time = datetime.fromisoformat(nasa_json[number]['date'])
        params = {'api_key': token}
        response = requests.get(
            f'https://api.nasa.gov/EPIC/archive/natural/{epic_time:%Y}/{epic_time:%m}/{epic_time:%d}/png/{epic_name}.png',
            params=params
        )
        response.raise_for_status()
        epics_url.append(response.url)
    return epics_url


def send_nasa_url(epics_url):
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
    get_photos_number = lambda: parser.parse_args().photos_number
    nasa_json = fetch_nasa_json(os.environ['NASA_TOKEN'])
    epics_url = fetch_nasa_url(os.environ['NASA_TOKEN'], get_photos_number(), nasa_json)
    send_nasa_url(epics_url)
