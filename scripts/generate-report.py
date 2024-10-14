import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from db import engine, DataLog
from sqlalchemy.orm import sessionmaker
from alert_processing.process_alerts import process_alerts
from report_generation.save_report import save_report
from datetime import datetime
from report_generation.analyze_data import analyze_data, dataPerSpecies

# default to today
date = datetime.now().strftime("%d-%m-%Y")

if len(sys.argv) > 1:
    # get day from args, eg. '13-10-2024'
    date = sys.argv[1]

def generate_report():
    print(f"Generating report for {date}")

    data = analyze_data(date)
    reportData = dataPerSpecies(data)
    
    save_report(date, reportData)

def data_exists():
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()
    data = session.query(DataLog).all()
    session.close()

    return len(data) > 0

if __name__ == "__main__":
    if not data_exists():
        print("ERROR: No data available to generate report. Please run the data generation script first.")
        exit(1)

    generate_report()
