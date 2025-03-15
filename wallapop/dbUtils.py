from db.mysql import MySQLConnection

class DBUtils:
    def __init__(self):
        self.mysql = MySQLConnection()
    
    def store_products(self, products, table):
        new_products = []
        updated_products = []

        for product in products:
            try:
                # Check if the product is already exists
                self.mysql.execute(
                    f"SELECT * FROM {table} WHERE url = %s",
                    (product["url"],)
                )
                result = self.mysql.fetchone()

                if result is None:
                    self.__insert_product(product, table)
                    new_products.append(product)
                elif result["price"] != product["price"]:
                    self.__insert_product(product, table)
                    updated_products.append(product)
                
            except Exception as e:
                print(f"Error storing product: {e}")
        
        print(f">> {len(new_products)} new products stored")
        print(f">> {len(updated_products)} products updated")

        return new_products, updated_products

    def close(self):
        self.mysql.close()

    # Private methods --------------------------------------------------------->>
    def __insert_product(self, product, table):
        self.mysql.execute(
            f"""
            INSERT INTO {table} (title, description, url, price)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            title = VALUES(title),
            description = VALUES(description),
            url = VALUES(url),
            price = VALUES(price)
            """,
            (product["title"], product["description"], product["url"], product["price"])
        )
        self.mysql.commit()
        print(f"+ Product stored: {product["title"]}")