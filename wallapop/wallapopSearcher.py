import wallapop.wallapopUtils as wallapopUtils
from utils.jsonParser import write_json
from utils.date import get_current_time
import requests

BASE_API_URL = "https://api.wallapop.com/api/v3/cars/search"
BASE_ITEM_URL = "https://es.wallapop.com/item/"

class WallapopSearcher:
    def search(self, config: dict) -> dict:
        result = []
        common_params = config["common_params"]
        specific_params = config["specific_params"]

        for item in specific_params:
            url = wallapopUtils.build_common_url(BASE_API_URL, common_params)
            url = wallapopUtils.add_specific_params(url, item)

            print(f"[{get_current_time(1)}] Searching for {item['brand']} {item['keywords']}...")

            response = requests.get(url)
            data = response.json()
            data = self.__extract_data_from_response__(data)

            brand = item["brand"] if item["brand"] != -1 else ""
            keywords = item["keywords"] if item["keywords"] != -1 else ""

            write_json(f"./output/{brand}_{keywords.replace(' ', '_')}.json", data)
            result.extend(data)
        
        return result
    
    def __extract_data_from_response__(self, response: dict) -> dict:
        objects = response["search_objects"]
        objects_data = []

        for obj in objects:
            obj_data = {
                "title": obj["content"]["title"],
                "description": obj["content"]["storytelling"],
                "status": self.__set_status__(obj["content"]["flags"]),
                "price": obj["content"]["price"],
                "location": obj["content"]["location"]["city"],
                "distance": obj["content"]["distance"],
                "brand": obj["content"]["brand"],
                "model": obj["content"]["model"],
                "version": obj["content"]["version"],
                "year": obj["content"]["year"],
                "kilometers": obj["content"]["km"],
                "fuel": obj["content"]["engine"],
                "gearbox": obj["content"]["gearbox"],
                "horsepower": obj["content"]["horsepower"],
                "creation_date": obj["content"]["creation_date"],
                "modification_date": obj["content"]["modification_date"],
                "url": BASE_ITEM_URL + obj["content"]["web_slug"]
            }

            objects_data.append(obj_data)
        
        return objects_data

    def __set_status__(self, flags: dict) -> str:
        return (
            "sold" if flags["sold"] else
            "reserved" if flags["reserved"] else
            "pending" if flags["pending"] else
            "banned" if flags["banned"] else
            "expired" if flags["expired"] else
            "onhold" if flags["onhold"] else
            "available"
        )