import json


config_file = open('config/config.json')
data = json.load(config_file)
config_file.close()

browsers_config = [browser for browser in data['browsers']]
headless_mode_config = data['headless_mode']