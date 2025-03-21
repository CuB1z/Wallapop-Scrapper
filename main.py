import schedule
from wallapop.wallapopSearcher import WallapopSearcher
from wallapop.dbUtils import DBUtils
from telegram.client import TelegramClient
from utils.date import get_current_time
from utils.jsonParser import parse_json

PRODUCTS_TABLE = "products"
CONFIG_FILE = "./wallapop/wallapopConfig.json"
INTERVAL = 20

def loop(config: dict):
    print(f"[{get_current_time(1)}] Starting a new search...")

    # Intialize dependencies
    wallapopSearcher = WallapopSearcher()
    tb_client = TelegramClient()
    db = DBUtils()

    # Search for the products
    products = wallapopSearcher.search(config)
    new_products, updated_products = db.store_products(products, PRODUCTS_TABLE)

    # Send the new products to the Telegram channel
    for product in new_products:
        message = tb_client.generate_new_products_message(product)
        tb_client.send_message(message)

    # Send the updated products to the Telegram channel
    for product in updated_products:
        message = tb_client.generate_updated_products_message(product)
        tb_client.send_message(message)


# [Main] ---------------------------------------------------------------------->>

if __name__ == "__main__":
    # Load the configuration file
    config = parse_json(CONFIG_FILE)
    loop(config)

    # Schedule the search to run every INTERVAL minutes
    schedule.every(INTERVAL).minutes.do(loop, config=config)
        
    while True:
        schedule.run_pending()