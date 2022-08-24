import telegram
import os
from dotenv import load_dotenv

load_dotenv()
tg_token = os.getenv("TG_TOKEN")
tg_chat_id = os.getenv("TG_CHAT_ID")

bot = telegram.Bot(token=tg_token)
print(bot.get_me())

bot.send_message(chat_id=tg_chat_id, text="I'm sorry Dave I'm afraid I can't do that.")

