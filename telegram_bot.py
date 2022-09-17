import os
import telegram
from dotenv import load_dotenv
import random
import argparse
import time


def publication_photo(all_images, token, chat_id, delay_time):
	bot = telegram.Bot(token=token)
	for image in all_images:
		with open(os.path.join('images', image), 'rb') as file:
			bot.send_document(chat_id=chat_id, document=file)
		time.sleep(delay_time)


def main(token, chat_id, delay_time):
	all_images = [image for image in os.walk("images")][0][2]
	while True:
		try:
			publication_photo(all_images, token, chat_id, delay_time)
			random.shuffle(all_images)
		except telegram.error.NetworkError:
			time.sleep(10)


if __name__ == "__main__":
	load_dotenv()
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
	tg_chat_id = os.environ['TG_CHAT_ID']
	tg_token = os.environ['TG_TOKEN']
	get_delay_time = lambda: parser.parse_args().delay_time
	main(tg_token, tg_chat_id, get_delay_time())

		