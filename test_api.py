from wallapop.wallapopSearcher import WallapopSearcher
from utils.jsonParser import parse_json

CONFIG_FILE = "./wallapop/newWallapopConfig.json"

scrapper = WallapopSearcher()
config = parse_json(CONFIG_FILE)
scrapper.search(config)