import telegram
import os
from dotenv import load_dotenv
import random
import argparse
import time
import requests


def publication_photo(all_images):
	for image in all_images:
		bot.send_document(
			channel_name, 
			document=open(f'images/{image}', 'rb')
		)
		time.sleep(args.delay_time)


if __name__ == "__main__":
	load_dotenv()
	tg_token = os.getenv("TG_TOKEN")
	tg_chat_id = os.getenv("TG_CHAT_ID")
	bot = telegram.Bot(token=tg_token)
	channel_name = '@devman_space_images'
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
	
	while True:
		all_images = [image for image in os.walk("images")][0][2]
		random.shuffle(all_images)
		publication_photo(all_images)
		exec(open("fetch_spacex_images.py").read())
		exec(open("fetch_nasas_images.py").read())
		exec(open("fetch_nasas_epic.py").read())
	
	