import dotenv

dotenv.load_dotenv()

from alert_processing.process_alerts import process_alerts

from report_generation.fetch_data import fetch_data

if __name__ == "__main__":
    process_alerts("11-10-2024")

    result = fetch_data("11-10-2024")
    print(result)
