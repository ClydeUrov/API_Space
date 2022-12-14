from pathlib import Path

import requests


def download_image(url, filename):
    Path("images").mkdir(parents=True, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, "wb") as file:
        file.write(response.content)
