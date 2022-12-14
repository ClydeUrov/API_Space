import argparse
import os

import requests

import download_space_image


class EmptyListError(ValueError):
    pass


def fetch_spacex_last_launch(launch):
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{launch}")
    response.raise_for_status()
    links = response.json()["links"]["flickr"]["original"]
    if not links:
        raise EmptyListError("Отсутствуют картинки в данном запуске")
    for number, spacex in enumerate(links):
        filename = os.path.join("images", f"spacex_{number}.jpg")
        download_space_image.download_image(spacex, filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Выгружает картинки SpaceX")
    parser.add_argument(
        "-d", dest="launch_id", help="ID запуска SpaceX", default="latest"
    )
    get_launch_id = lambda: parser.parse_args().launch_id
    fetch_spacex_last_launch(get_launch_id())
