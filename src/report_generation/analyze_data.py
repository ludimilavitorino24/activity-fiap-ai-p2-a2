import dotenv
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from db import engine
from db_utils import fetch_datalogs
from typings import ReportData

dotenv.load_dotenv()

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

def analyze_data(analysis_date: str = datetime.now().strftime("%d-%m-%Y")):
    """
    Analyze the data for a given date.

    Args:
        analysis_date (str): The date to analyze in the format 'DD-MM-YYYY'. Defaults to today.

    Returns:
        dict: A dictionary containing the analyzed data.
    """
    df = fetch_datalogs(analysis_date)

    data = {}

    for species_id, species_group in df.groupby("id_species"):
        species_name = species_group["species_name"].iloc[0]
        data[species_name] = {}

        for breed_id, breed_group in species_group.groupby("id_breed"):
            breed_name = breed_group["breed_name"].iloc[0]

            animal_distances_traveled = breed_group.groupby("id_animal").agg(
                {"total_animal_distance_traveled": "first"}
            )

            data[species_name][breed_name] = {
                "count": breed_group["id_animal"].nunique(),
                "mean_temperature": round(float(breed_group["temperature"].mean()), 2),
                "max_temperature": round(float(breed_group["temperature"].max()), 2),
                "min_temperature": round(float(breed_group["temperature"].min()), 2),
                "mean_heartrate": round(float(breed_group["heartrate"].mean()), 2),
                "max_heartrate": round(float(breed_group["heartrate"].max()), 2),
                "min_heartrate": round(float(breed_group["heartrate"].min()), 2),
                "total_distance_traveled_meters": round(
                    float(animal_distances_traveled.sum().iloc[0]), 2
                ),
                "mean_distance_traveled_meters": round(
                    float(animal_distances_traveled.mean().iloc[0]), 2
                ),
                "max_distance_traveled_meters": round(
                    float(animal_distances_traveled.max().iloc[0]), 2
                ),
                "min_distance_traveled_meters": round(
                    float(animal_distances_traveled.min().iloc[0]), 2
                ),
            }

    return data

def dataPerSpecies(data):
    reportData = []

    for species, species_data in data.items():
        for breed, breed_data in species_data.items():
            reportData.append(ReportData(species, breed, breed_data['count'], breed_data['mean_temperature'], breed_data['max_temperature'], breed_data['min_temperature'], breed_data['total_distance_traveled_meters'], breed_data['mean_distance_traveled_meters'], breed_data['max_distance_traveled_meters'], breed_data['min_distance_traveled_meters']))

    return reportData
