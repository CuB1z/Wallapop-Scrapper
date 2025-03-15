from dotenv import load_dotenv
from telebot import TeleBot
import os

class TelegramClient:
    def __init__(self):
        # Load the environment variables
        load_dotenv()

        # Get the token and chat id from the environment variables
        self.token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.ch_id = os.getenv("CHAT_ID")

        # Create the bot
        self.tb = TeleBot(self.token)

    def send_message(self, message):
        try:
            self.tb.send_message(self.ch_id, message)
            print("[+] Message sent correctly")
        except Exception as e:
            print(f"[-] Error sending the message: {e}")