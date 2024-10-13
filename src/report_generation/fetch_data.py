import dotenv
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from db import engine
from db_utils import fetch_datalogs

dotenv.load_dotenv()

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()


def fetch_data(analysis_date: str = datetime.now().strftime("%d-%m-%Y")):
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
                    float(animal_distances_traveled.sum()), 2
                ),
                "mean_distance_traveled_meters": round(
                    float(animal_distances_traveled.mean()), 2
                ),
                "max_distance_traveled_meters": round(
                    float(animal_distances_traveled.max()), 2
                ),
                "min_distance_traveled_meters": round(
                    float(animal_distances_traveled.min()), 2
                ),
            }

    return data
