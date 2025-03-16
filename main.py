import schedule
import time
from textwrap import dedent
from wallapop.wallapopScrapper import WallapopScraper
from wallapop.dbUtils import DBUtils
from telegram.client import TelegramClient
from utils.date import get_current_time
from utils.jsonParser import parse_json

PRODUCTS_TABLE = "products"
CONFIG_FILE = "./wallapop/wallapopConfig.json"
INTERVAL = 20

def generate_new_products_message(product: dict) -> str:
    return dedent(f"""
    🆕 Nuevo Producto!!
    🚗 {product["title"]}

    📝 Descripción
    {product["description"]}

    💰 {product["price"]}
    📌 {product["url"]}
    """)

def generate_updated_products_message(product: dict) -> str:
    return dedent(f"""
    🔄 Producto actualizado!!
    🚗 {product["title"]}

    💰 {product["price"]}
    📌 {product["url"]}
    """)

def scrape_and_notify(params: dict):
    # Initialize dependencies
    scraper = WallapopScraper()
    db = DBUtils()
    tb_client = TelegramClient()

    # Scrape the products
    products = scraper.scrape(params)
    scraper.close()

    # Store the products in the database
    new_products, updated_products = db.store_products(products, PRODUCTS_TABLE)
    db.close()

    # Send the new products to the Telegram channel
    for product in new_products:
        message = generate_new_products_message(product)
        tb_client.send_message(message)

    # Send the updated products to the Telegram channel
    for product in updated_products:
        message = generate_updated_products_message(product)
        tb_client.send_message(message)

    print(f"> Updated products at {get_current_time(1)} -- {len(updated_products) + len(new_products)} products updated")

def scrape_all(config):
    params = config["params"]
    keywords = config["keywords"]

    for keyword in keywords:
        print(f"> Searching for: {keyword}")
        params["keywords"] = keyword
        scrape_and_notify(params)


# [Main] ---------------------------------------------------------------------->>

if __name__ == "__main__":
    # Load the configuration file
    scrape_config = parse_json(CONFIG_FILE)

    # Run initial scrape
    scrape_all(scrape_config)

    # Schedule the search to run every INTERVAL minutes
    schedule.every(INTERVAL).minutes.do(scrape_all, config=scrape_config)
        
    while True:
        schedule.run_pending()
        time.sleep(1)