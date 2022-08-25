import os
import requests
from pathlib import Path
from os.path import splitext
from dotenv import load_dotenv


def download_image(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_nasa_epic(token):
    params = {'api_key': token}
    response = requests.get(
      'https://api.nasa.gov/EPIC/api/natural/images',
      params=params
    )
    all_epic = response.json()
    epics_url = []
    
    for number in range(0, 5):
        epic_name = all_epic[number]['image']
        splited_epic = all_epic[number]['date'].split(' ')
        splited_epic = splited_epic[0].split('-')
           
        response = requests.get(
          f'https://api.nasa.gov/EPIC/archive/natural/{splited_epic[0]}/{splited_epic[1]}/{splited_epic[2]}/png/{epic_name}.png',
          params=params
        )
        epics_url.append(response.url)
    
        for nasa_epic_number, epic in enumerate(epics_url):
            filename = 'images/nasa_epic_{}.png'.format(nasa_epic_number)
            download_image(epic, filename)


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.getenv("NASA_TOKEN")
    Path("images").mkdir(parents=True, exist_ok=True)
    fetch_nasa_epic(nasa_token)