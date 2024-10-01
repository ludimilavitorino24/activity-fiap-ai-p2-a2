import dotenv
dotenv.load_dotenv()

import data_simulation.main
import report_generation.main
import alert_processing.main
from report_generation.fetch_data import fetch_data

if __name__ == "__main__":
    result = fetch_data()
    print("result", result)