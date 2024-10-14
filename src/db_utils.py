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

def fetch_datalogs(
    analysis_date: str = datetime.now().strftime("%d-%m-%Y"),
) -> pd.DataFrame:
    dt = datetime.strptime(analysis_date, "%d-%m-%Y")
    print("Fetching data for date:", analysis_date)

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
            datalog.id_animal_collar as id_animal_collar,
            cast(datalog.temperature as float) as temperature,
            cast(datalog.heartrate as float) as heartrate,
            cast(datalog.latitude as float) as latitude,
            cast(datalog.longitude as float) as longitude,
            datalog.created_at as created_at,
            datalog.updated_at as updated_at
        FROM t_wc_datalog datalog
        LEFT JOIN t_wc_animals_collars animal_collars ON datalog.id_animal_collar = animal_collars.id_animal_collar
        LEFT JOIN t_wc_animals animals ON animal_collars.id_animal = animals.id_animal
        LEFT JOIN t_wc_species species ON animals.id_species = species.id_species
        LEFT JOIN t_wc_breeds breeds ON animals.id_breed = breeds.id_breed
        WHERE cast(datalog.created_at as Date) = '{dt.strftime("%Y-%m-%d")}'
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
            "id_animal_collar",
            "temperature",
            "heartrate",
            "latitude",
            "longitude",
            "created_at",
            "updated_at",
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

    animal_distances_traveled = df.groupby("id_animal").apply(
        calculate_total_distance_animal
    )

    df["total_animal_distance_traveled"] = df["id_animal"].map(
        animal_distances_traveled
    )

    return df

# t_wc_alerts table
# class Alert(Base):
#     __tablename__ = 't_wc_alerts'

#     id_alert = Column(Integer, primary_key=True, autoincrement=True)
#     id_datalog = Column(Integer, ForeignKey(f'{SCHEMA}.t_wc_datalog.id_datalog'), nullable=False)
#     alert_metric = Column(String(50), nullable=False)  # e.g., 'temperature', 'heartrate', 'movement'
#     alert_type = Column(String(50), nullable=False)  # e.g. 'z_score_outlier_above', 'z_score_outlier_below'
#     created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

#     datalog = relationship('DataLog')
    
#     __str__ = lambda self: f'Alert {self.alert_type} for Animal Collar {self.id_animal_collar}'

def fetch_alerts(
    analysis_date: str = datetime.now().strftime("%d-%m-%Y")
) -> pd.DataFrame:
    dt = datetime.strptime(analysis_date, "%d-%m-%Y")
    print("Fetching alerts for date:", analysis_date)

    query = f"""
        -- sql
        SELECT 
            alerts.id_alert,
            alerts.id_datalog,
            alerts.alert_metric,
            alerts.alert_type,
            alerts.created_at,
            datalog.id_animal_collar,
            datalog.temperature,
            datalog.heartrate,
            datalog.latitude,
            datalog.longitude,
            datalog.created_at as datalog_created_at,
            datalog.updated_at as datalog_updated_at,
            species.id_species,
            species.name as species_name,
            breeds.id_breed,
            breeds.name as breed_name
        FROM t_wc_alerts alerts
        LEFT JOIN t_wc_datalog datalog ON alerts.id_datalog = datalog.id_datalog
        LEFT JOIN t_wc_animals_collars animal_collars ON datalog.id_animal_collar = animal_collars.id_animal_collar
        LEFT JOIN t_wc_animals animals ON animal_collars.id_animal = animals.id_animal
        LEFT JOIN t_wc_species species ON animals.id_species = species.id_species
        LEFT JOIN t_wc_breeds breeds ON animals.id_breed = breeds.id_breed
        WHERE cast(alerts.created_at as Date) = '{dt.strftime("%Y-%m-%d")}'
    """

    result = session.execute(text(query)).fetchall()

    df = pd.DataFrame(
        result,
        columns=[
            "id_alert",
            "id_datalog",
            "alert_metric",
            "alert_type",
            "created_at",
            "id_animal_collar",
            "temperature",
            "heartrate",
            "latitude",
            "longitude",
            "datalog_created_at",
            "datalog_updated_at",
            "id_species",
            "species_name",
            "id_breed",
            "breed_name",
        ],
    )

    return df

def generate_alerts_counts(day):
    df = fetch_alerts(day)
    
    data = {}

    for species_id, species_group in df.groupby("id_species"):
        species_name = species_group["species_name"].iloc[0]
        data[species_name] = {}

        for breed_id, breed_group in species_group.groupby("id_breed"):
            breed_name = breed_group["breed_name"].iloc[0]
            data[species_name][breed_name] = {}

            for alert_metric, metric_group in breed_group.groupby("alert_metric"):
                data[species_name][breed_name][alert_metric] = {}

                for alert_type, alert_type_group in metric_group.groupby("alert_type"):
                    data[species_name][breed_name][alert_metric][alert_type] = len(
                        alert_type_group
                    )
    
    return data