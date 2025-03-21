from dotenv import load_dotenv
from telebot import TeleBot
from time import sleep
from textwrap import dedent
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
            self.tb.send_message(self.ch_id, message, parse_mode="Markdown")
            print("  [+] Message sent correctly")
            sleep(3)
        except Exception as e:
            print(f"[-] Error sending the message: {e}")
    
    def generate_new_products_message(self, product: dict) -> str:
        return (
            f"🆕 *Nuevo Producto!!*\n"
            f"🚗 *{product['title']}*\n\n"
            f"📍 *{product['location']}*\n\n"
            f"📝 *Descripción*\n"
            f"{product['description']}\n\n"
            f"💰 *Precio:* {int(product['price'])} €\n\n"
            f"📌 [Ver en Wallapop]({product['url']})\n"
        )

    def generate_updated_products_message(self, product: dict) -> str:
        return (
            f"🔄 *Producto actualizado!!*\n"
            f"🚗 *{product['title']}*\n\n"
            f"💰 *Precio:* {int(product['price'])} €\n\n"
            f"📌 [Ver en Wallapop]({product['url']})\n"
        )