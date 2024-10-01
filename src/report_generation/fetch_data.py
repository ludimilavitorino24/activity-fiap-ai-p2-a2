import dotenv
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy import func, cast, Date, text

from db import engine, DataLog, Species, Breed, Animal, AnimalCollar

dotenv.load_dotenv()

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()


def fetch_data(analysis_date: str = datetime.now().strftime("%d-%m-%Y")):
    analysis_date = datetime.strptime(analysis_date, "%d-%m-%Y")

    query = f"""
    SELECT 
        count(*) as quantity, 
        avg(datalog.temperature) as mean_temperature,
        max(datalog.temperature) as max_temperature,
        min(datalog.temperature) as min_temperature
    FROM t_wc_datalog datalog
    LEFT JOIN t_wc_animals_collars animal_collars ON datalog.id_animal_collar = animal_collars.id_animal_collar
    LEFT JOIN t_wc_animals animals ON animal_collars.id_animal = animals.id_animal
    LEFT JOIN t_wc_species species ON animals.id_species = species.id_species
    LEFT JOIN t_wc_breeds breeds ON animals.id_breed = breeds.id_breed
    WHERE datalog.created_at = '{analysis_date}'
    GROUP BY animals.id_species, animals.id_breed
    """

    result = session.execute(text(query)).fetchall()

    return result
