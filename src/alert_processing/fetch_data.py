import dotenv
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy import text
import pandas as pd

from db import engine
from utils import calculate_distance_meters

dotenv.load_dotenv()

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()


def fetch_data(analysis_date: str = datetime.now().strftime("%d-%m-%Y")):
    print("Fetching data for date:", analysis_date)
    analysis_date = datetime.strptime(analysis_date, "%d-%m-%Y")

    query = f"""
        -- sql
        SELECT 
            id_datalog as id_datalog,
            species.id_species as id_species,
            species.name as species_name,
            breeds.id_breed as id_breed,
            breeds.name as breed_name,
            animals.id_animal as id_animal,
            animals.name as animal_name,
            cast(datalog.temperature as float) as temperature,
            cast(datalog.heartrate as float) as heartrate,
            cast(datalog.latitude as float) as latitude,
            cast(datalog.longitude as float) as longitude,
            datalog.created_at as created_at,
            datalog.updated_at as updated_at,
            datalog.is_outlier as is_outlier
        FROM t_wc_datalog datalog
        LEFT JOIN t_wc_animals_collars animal_collars ON datalog.id_animal_collar = animal_collars.id_animal_collar
        LEFT JOIN t_wc_animals animals ON animal_collars.id_animal = animals.id_animal
        LEFT JOIN t_wc_species species ON animals.id_species = species.id_species
        LEFT JOIN t_wc_breeds breeds ON animals.id_breed = breeds.id_breed
        WHERE cast(datalog.created_at as Date) = '{analysis_date}'
    """

    result = session.execute(text(query)).fetchall()

    df = pd.DataFrame(
        result,
        columns=[
            "id_datalog",
            "id_species",
            "species_name",
            "id_breed",
            "breed_name",
            "id_animal",
            "animal_name",
            "temperature",
            "heartrate",
            "latitude",
            "longitude",
            "created_at",
            "updated_at",
            "is_outlier",
        ],
    )

    df = df.sort_values(by=["id_animal", "created_at"])

    def calculate_total_distance_animal(animal_df: pd.DataFrame):
        total_distance = 0
        for i in range(1, len(animal_df)):
            lat1 = animal_df.iloc[i - 1]["latitude"]
            lon1 = animal_df.iloc[i - 1]["longitude"]
            lat2 = animal_df.iloc[i]["latitude"]
            lon2 = animal_df.iloc[i]["longitude"]
            total_distance += calculate_distance_meters(lat1, lon1, lat2, lon2)
        return total_distance

    df["animal_distance_traveled"] = 0.0

    for animal_id, animal_df in df.groupby("id_animal"):
        distances = [0.0]
        for i in range(1, len(animal_df)):
            lat1 = animal_df.iloc[i - 1]["latitude"]
            lon1 = animal_df.iloc[i - 1]["longitude"]
            lat2 = animal_df.iloc[i]["latitude"]
            lon2 = animal_df.iloc[i]["longitude"]
            distance = calculate_distance_meters(lat1, lon1, lat2, lon2)
            distances.append(distance)
        df.loc[animal_df.index, "animal_distance_traveled"] = distances

    animal_distance_traveled = df.groupby("id_animal").apply(
        calculate_total_distance_animal
    )

    df["total_animal_distance_traveled"] = df["id_animal"].map(animal_distance_traveled)

    # with pd.option_context("display.max_columns", None, "display.max_rows", None):
    #     print("Calculating distance traveled by each animal")
    #     print(df.iloc[280:300])

    return df
