from wallapop.wallapopScrapper import WallapopScraper
from wallapop.dbUtils import DBUtils

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
        "keywords": ""
    }

    PRODUCTS_TABLE = "products"

    # Initialize the scraper and the database utilities
    scraper = WallapopScraper()
    db = DBUtils()

    # Scrape the products
    products = scraper.scrape(params)
    scraper.close()

    # Store the products in the database
    new_products, updated_products = db.store_products(products, PRODUCTS_TABLE)
    db.close()