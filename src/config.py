import json
import os

#region Default Config

DEFAULT_CONFIG = {
    "simulation": {
        "animalNumber": 2,
        "interval": 5,
        "iterations": 4
    },
    "report": {
        "outDir": "./reports/",
    }
}

def saveDefaultConfig():
    try:
        with open("config.json", "x") as f:
            f.write(json.dumps(DEFAULT_CONFIG, indent=4))
    except FileExistsError:
        pass

saveDefaultConfig()

#endregion

#region Config

config = DEFAULT_CONFIG

with open("config.json", "r") as f:
    config = json.load(f)

#endregion

#region Values

animalNumber = config.get('simulation', {}).get('animalNumber', DEFAULT_CONFIG['simulation']['animalNumber'])
interval = config.get('simulation', {}).get('interval', DEFAULT_CONFIG['simulation']['interval'])
iterations = config.get('simulation', {}).get('iterations', DEFAULT_CONFIG['simulation']['iterations'])
reportOutDir = config.get('report', {}).get('outDir', DEFAULT_CONFIG['report']['outDir'])

#endregion
