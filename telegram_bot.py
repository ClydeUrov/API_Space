import os
import telegram
from dotenv import load_dotenv
import random
import argparse
import time
import requests

 
def publication_photo(all_images):
	for image in all_images:
		with open(os.path.join('images', f'{image}'), 'rb') as file:
			bot.send_document(
				chat_id=tg_chat_id,
				document=file
			)
			file.close()
		time.sleep(args.delay_time)


def main():
	all_images = [image for image in os.walk("images")][0][2]
	publication_photo(all_images)
	while True:
		random.shuffle(all_images)
		publication_photo(all_images)


if __name__ == "__main__":
	load_dotenv()
	tg_token = os.environ.get("TG_TOKEN")
	tg_chat_id = os.environ.get("TG_CHAT_ID")
	bot = telegram.Bot(token=tg_token)
	parser = argparse.ArgumentParser(
		description="Размещает фото на телеграмм канал"
	)
	parser.add_argument(
		'-d',
		dest='delay_time',
		help='Время задержки',
		default=14400,
		type=int
	)
	args = parser.parse_args()
	try:
		main()
	except requests.ConnectionError:
		main()
	except telegram.error.NetworkError:
		main()
		