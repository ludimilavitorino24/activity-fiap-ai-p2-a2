import dotenv
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from db import engine
from db_utils import fetch_datalogs

dotenv.load_dotenv()

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()


def fetch_data(analysis_date: str = datetime.now().strftime("%d-%m-%Y")):
    return fetch_datalogs(analysis_date)
