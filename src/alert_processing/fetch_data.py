import dotenv
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy import text
import pandas as pd

from db import engine
from db_utils import fetch_datalogs
from utils import calculate_distance_meters

dotenv.load_dotenv()

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()


def fetch_data(analysis_date: str = datetime.now().strftime("%d-%m-%Y")):
    return fetch_datalogs(analysis_date)
