import json

DEFAULT_CONFIG = {
    "simulation": {
        "animalNumber": 2,
        "interval": 5,
        "iterations": 4
    }
}

config = DEFAULT_CONFIG

with open("config.json", "r") as f:
    config = json.load(f)

animalNumber = config.get('simulation', {}).get('animalNumber', DEFAULT_CONFIG['simulation']['animalNumber'])
interval = config.get('simulation', {}).get('interval', DEFAULT_CONFIG['simulation']['interval'])
iterations = config.get('simulation', {}).get('iterations', DEFAULT_CONFIG['simulation']['iterations'])
