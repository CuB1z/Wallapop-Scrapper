from wallapop.wallapopScrapper import WallapopScraper
from wallapop.dbUtils import DBUtils
from telegram.client import TelegramClient
from textwrap import dedent

if __name__ == "__main__":
    params = {
        "category_ids": 100,
        "filters_source": "search_box",
        "latitude": 40.41956,
        "longitude": -3.69196,
        "max_sale_price": 3000,
        "min_km": 1000,
        "max_km": 250000,
        "min_year": 2000,
        "max_year": 2008,
        "min_horse_power": 100,
        "time_filter": "today",
        "order_by": "newest",
        "keywords": "bmw"
    }

    PRODUCTS_TABLE = "products"

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
        message = dedent(f"""
        🆕 Nuevo Producto!!
        🚗 {product["title"]}

        📝 Descripción
        {product["description"]}

        💰 {product["price"]}
        📌 {product["url"]}
        """)

        tb_client.send_message(message)

    # Send the updated products to the Telegram channel
    for product in updated_products:
        message = dedent(f"""
        🔄 Producto actualizado!!
        🚗 {product["title"]}

        💰 {product["price"]}
        📌 {product["url"]}
        """)

        tb_client.send_message(message)