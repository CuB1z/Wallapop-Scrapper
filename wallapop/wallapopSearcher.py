from utils.jsonParser import write_json
import requests
from urllib.parse import urlencode

BASE_API_URL = "https://api.wallapop.com/api/v3/cars/search"

class WallapopSearcher:
    def search(self, config: dict) -> dict:
        common_params = config["common_params"]
        specific_params = config["specific_params"]

        for item in specific_params:
            url = self.__build_common_url(BASE_API_URL, common_params)
            url = self.__add_specific_params(url, item)

            response = requests.get(url)
            data = response.json()
            write_json(f"./output/{item["brand"]}_{item["keywords"].replace(' ', '_')}.json", data)

    def __build_common_url(self, url: str, common_params: dict) -> str:
        url += "?"
        for key, value in common_params.items():
            if value != -1:
                url += f"{key}={value}&"

        return url

    def __add_specific_params(self, url: str, specific_params: dict) -> str:
        for key, value in specific_params.items():
            url += f"{key}={value.replace(" ", "_")}"

        return url