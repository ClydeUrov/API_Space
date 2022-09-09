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
				chat_id=os.environ.get("TG_CHAT_ID"),
				document=file
			)
			file.close()
		time.sleep(args.delay_time)


def main():
	all_images = [image for image in os.walk("images")][0][2]
	while True:
		try:
			publication_photo(all_images)
			random.shuffle(all_images)
		except telegram.error.NetworkError:
			time.sleep(10)
			main()
		except requests.ConnectionError:
			time.sleep(10)
			main()


if __name__ == "__main__":
	load_dotenv()
	os.environ['TG_TOKEN'] = str(input('Введите ваш TG_TOKEN: '))
	os.environ['TG_CHAT_ID'] = str(input('Введите ваш TG_CHAT_ID: '))
	bot = telegram.Bot(token=os.environ.get("TG_TOKEN"))
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
	main()

		