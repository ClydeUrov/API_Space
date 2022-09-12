import os
import telegram
from dotenv import load_dotenv
import random
import argparse
import time


def publication_photo(all_images, bot, tg_chat_id):
	for image in all_images:
		with open(os.path.join('images', image), 'rb') as file:
			bot.send_document(
				chat_id=tg_chat_id,
				document=file
			)
		time.sleep(args.delay_time)


def main():
	redefine_tg_env = input("Желаете ли переопределить TG_TOKEN и TG_CHAT_ID? ")
	if redefine_tg_env == "Yes" or redefine_tg_env == "Да":
		os.environ['TG_TOKEN'] = str(input('Введите ваш TG_TOKEN: '))
		os.environ['TG_CHAT_ID'] = str(input('Введите ваш TG_CHAT_ID: '))

	bot = telegram.Bot(token=os.environ.get("TG_TOKEN"))
	tg_chat_id = os.environ.get("TG_CHAT_ID")
	all_images = [image for image in os.walk("images")][0][2]
	while True:
		try:
			publication_photo(all_images, bot, tg_chat_id)
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
	args = parser.parse_args()
	main()

		