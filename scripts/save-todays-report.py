import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from db import engine, DataLog
from sqlalchemy.orm import sessionmaker
from alert_processing.process_alerts import process_alerts
from report_generation.save_report import save_report

def save_todays_report():
    process_alerts('13-10-2024') #fix it
    # read alerts
    # transform data
    # save-report
    reportData = []
    save_report('13-10-2024', reportData) #fix it

def data_exists():
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()
    data = session.query(DataLog).all()
    session.close()

    return len(data) > 0

if __name__ == "__main__":
    if not data_exists():
        print("ERROR: No data available to generate report.")
        exit(1)

    save_todays_report()
