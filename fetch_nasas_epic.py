import os
import requests
from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime
import download_space_image
import argparse


def fetch_nasa_epic(token):
    params = {'api_key': token}
    epic_response = requests.get(
      'https://api.nasa.gov/EPIC/api/natural/images',
      params=params
    )
    epics_url = []
    for number in range(0, photos_number()):
        epic_name = epic_response.json()[number]['image']
        epic_time = datetime.fromisoformat(epic_response.json()[number]['date'])
        response = requests.get(
          f'https://api.nasa.gov/EPIC/archive/natural/{epic_time.year}/{epic_time.strftime("%m")}/{epic_time.strftime("%d")}/png/{epic_name}.png',
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
        help='Колличество скачиваемых фотографий NASA EPIC.',
        default='5',
        type=int
    )
    photos_number = lambda: parser.parse_args().photos_number
    redefine_nasa_env = input("Желаете ли переопределить NASA_TOKEN? ")
    if redefine_nasa_env == "Yes" or redefine_nasa_env == "Да":
        os.environ['NASA_TOKEN'] = str(input('Введите ваш NASA_TOKEN: '))
    Path("images").mkdir(parents=True, exist_ok=True)
    fetch_nasa_epic(os.environ.get('NASA_TOKEN'))
