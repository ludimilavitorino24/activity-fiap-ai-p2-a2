import json
import os

# region Default Config

DEFAULT_CONFIG = {
    "simulation": {
        "animalNumber": 2,
        "interval": 5,
        "iterations": 4
    },
    "report": {
        "outDir": "./reports/",
        "templatePath": "./config/template.jinja2.md"
    },
    "alerts": {
        "temperature_outlier_z_threshold": 3.2,
        "hearth_rate_outlier_z_threshold": 6.0,
        "movement_outlier_z_threshold": 1.7,
    },
}

def saveDefaultConfig():
    try:
        with open("config/config.json", "x") as f:
            f.write(json.dumps(DEFAULT_CONFIG, indent=4))
    except FileExistsError:
        pass

saveDefaultConfig()

# endregion

# region Config

config = DEFAULT_CONFIG

with open("config/config.json", "r") as f:
    config = json.load(f)

# endregion

# region Values

animalNumber = config.get('simulation', {}).get('animalNumber', DEFAULT_CONFIG['simulation']['animalNumber'])
interval = config.get('simulation', {}).get('interval', DEFAULT_CONFIG['simulation']['interval'])
iterations = config.get('simulation', {}).get('iterations', DEFAULT_CONFIG['simulation']['iterations'])
reportOutDir = config.get('report', {}).get('outDir', DEFAULT_CONFIG['report']['outDir'])
templatePath = config.get('report', {}).get('templatePath', DEFAULT_CONFIG['report']['templatePath'])

temperature_outlier_z_threshold = config.get("alerts", {}).get(
    "temperature_outlier_z_threshold",
    DEFAULT_CONFIG["alerts"]["temperature_outlier_z_threshold"],
)
hearth_rate_outlier_z_threshold = config.get("alerts", {}).get(
    "hearth_rate_outlier_z_threshold",
    DEFAULT_CONFIG["alerts"]["hearth_rate_outlier_z_threshold"],
)
movement_outlier_z_threshold = config.get("alerts", {}).get(
    "movement_outlier_z_threshold",
    DEFAULT_CONFIG["alerts"]["movement_outlier_z_threshold"],
)

# endregion
