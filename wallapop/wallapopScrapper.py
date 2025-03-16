from urllib.parse import urlencode
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://es.wallapop.com/app/search"

class WallapopScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 60)

    def scrape(self, params: dict):
        full_url = self.__build_url(BASE_URL, params)
        print(f">> Scraping URL: {full_url}")
        self.driver.get(full_url)

        # Accept the consent button
        accept_button = self.wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
        accept_button.click()

        # Wait for search results to load and retrieve all products
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ItemCardList__item")))
        products = self.driver.find_elements(By.CLASS_NAME, "ItemCardList__item")

        # Create a list with the details of the products
        product_list = []
        for product in products:
            try:
                title = product.get_attribute("title")
                url = product.get_attribute("href")
                price = product.find_element(By.CLASS_NAME, "ItemCardWide__price").text
                description_elements = product.find_elements(By.CLASS_NAME, "ItemCardWide__description")

                if description_elements:
                    description = description_elements[0].text
                else:
                    description = "No description available"
                
                product = {
                    "title": title,
                    "description": description,
                    "url": url,
                    "price": price
                }

                product_list.append(product)
            except Exception as e:
                print(f"Error processing product: {e}")

        print(f">> Scraping finished with {len(product_list)} products")
        return product_list

    def close(self):
        self.driver.quit()

    def __build_url(self, url: str, params: dict):
        return f"{url}?{urlencode(params)}"