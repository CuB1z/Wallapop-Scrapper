import wallapop.wallapopUtils as wallapopUtils
from utils.jsonParser import write_json
from utils.date import get_current_time
import requests

BASE_API_URL = "https://api.wallapop.com/api/v3/cars/search"
BASE_ITEM_URL = "https://es.wallapop.com/item/"

class WallapopSearcher:
    def __map_fuel_value(self, wallapop_fuel):
        """Mapea los valores de combustible de Wallapop al ENUM de la base de datos"""
        if not wallapop_fuel or wallapop_fuel.strip() == "":
            return "Other"
        
        fuel_mapping = {
            'diesel': 'Gasoil',
            'gasoil': 'Gasoil', 
            'gasoline': 'Gasoline',
            'petrol': 'Gasoline',
            'electric': 'Electric',
            'hybrid': 'Hybrid'
        }
        return fuel_mapping.get(wallapop_fuel.lower(), 'Other')

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
                "title": obj["content"]["title"] if "title" in obj["content"] else "",
                "description": obj["content"]["storytelling"] if "storytelling" in obj["content"] else "",
                "status": self.__set_status__(obj["content"]["flags"]),
                "price": obj["content"]["price"] if "price" in obj["content"] else 0,
                "location": obj["content"]["location"]["city"] if "city" in obj["content"]["location"] else "Unknown",
                "distance": obj["content"]["distance"] if "distance" in obj["content"] else 0,
                "brand": obj["content"]["brand"] if "brand" in obj["content"] else "",
                "model": obj["content"]["model"] if "model" in obj["content"] else "",
                "version": obj["content"]["version"] if "version" in obj["content"] else "",
                "year": obj["content"]["year"] if "year" in obj["content"] else 0,
                "kilometers": obj["content"]["km"] if "km" in obj["content"] else 0,
                "fuel": self.__map_fuel_value(obj["content"]["engine"]) if "engine" in obj["content"] else "Other",
                "gearbox": obj["content"]["gearbox"] if "gearbox" in obj["content"] else "",
                "horsepower": obj["content"]["horsepower"] if "horsepower" in obj["content"] else 0,
                "creation_date": obj["content"]["creation_date"] if "creation_date" in obj["content"] else "",
                "modification_date": obj["content"]["modification_date"] if "modification_date" in obj["content"] else "",
                "url": BASE_ITEM_URL + obj["content"]["web_slug"] if "web_slug" in obj["content"] else ""
            }

            # Debug temporal: ver el mapeo
            original_fuel = obj["content"]["engine"] if "engine" in obj["content"] else ""


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