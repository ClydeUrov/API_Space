import requests
from pathlib import Path


def download_image(url, filename):
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    response = requests.get(
        'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    )
    res = response.json()
    spacex_links = (res['links']['flickr']['original'])
    
    for spacex_number, spacex in enumerate(spacex_links):
        filename = f'images/spacex_{spacex_number}.jpg'
        download_image(spacex, filename)

if __name__ == "__main__":
    Path("images").mkdir(parents=True, exist_ok=True)
    fetch_spacex_last_launch()
