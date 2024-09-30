import dotenv
dotenv.load_dotenv()

from data_simulation.main import generate_cow_temp_data
from db import engine, Collar, Animal, DataLog, AnimalCollar, Breed, Species
from sqlalchemy.orm import sessionmaker

def populate_db():
    data = generate_cow_temp_data() 

    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()

    new_species = Species(
        name="Cow"
    )
    session.add(new_species)
    session.commit()

    new_breed = Breed(
        name="Holstein"
    )
    session.add(new_breed)
    session.commit()



    new_animal = Animal(
        tag_id=1,
        name="Betsy",
        id_species=new_species.id_species,
        id_breed=new_breed.id_breed
    )
    session.add(new_animal)
    session.commit()

    new_collar = Collar()
    session.add(new_collar)
    session.commit()

    new_animal_collar = AnimalCollar(
        id_collar=new_collar.id_collar,
        id_animal=new_animal.id_animal
    )
    session.add(new_animal_collar)
    session.commit()

    new_datalog = DataLog(
        id_animal_collar=new_animal_collar.id_animal_collar,
        temperature=data[0]
    )
    session.add(new_datalog)
    session.commit()

    session.close()

if __name__ == "__main__":
    populate_db()