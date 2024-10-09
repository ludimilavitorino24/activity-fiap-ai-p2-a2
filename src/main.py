import dotenv

dotenv.load_dotenv()

from alert_processing.process_alerts import process_alerts

# from report_generation.fetch_data import fetch_data

if __name__ == "__main__":
    result = process_alerts("01-10-2024")
    print(result)
    assert False
    # print("Data for report:", result)
    # result = fetch_data("01-10-2024")
    # print(result)
