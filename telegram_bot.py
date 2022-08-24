import telegram
import os
from dotenv import load_dotenv

load_dotenv()
tg_token = os.getenv("TG_TOKEN")
tg_chat_id = os.getenv("TG_CHAT_ID")

bot = telegram.Bot(token=tg_token)
print(bot.get_me())

bot.send_document(chat_id=TG_CHAT_ID, document=open('images/nasa_apod_12', 'rb'))

# updates = bot.get_updates()
# print([u.message.photo for u in updates if u.message.photo])