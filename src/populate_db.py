import dotenv
dotenv.load_dotenv()

from data_simulation.main import next_temp, next_heartrate, next_geo2d
from db import engine, Collar, Animal, DataLog, AnimalCollar, Breed, Species
from sqlalchemy.orm import sessionmaker
from config import animalNumber, interval, iterations
from datetime import datetime
import random
from data_simulation.animal_names import cow_names_pt_br

def populate_db():
    try:
        SessionLocal = sessionmaker(bind=engine)
        session = SessionLocal()

        #region Create Species and Breed

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

        #endregion

        for i in range(animalNumber):
            animal_name = random.choice(cow_names_pt_br)
            new_animal = Animal(
                tag_id=1,
                name=animal_name + " " + str(i + 1),
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
            
            for j in range(iterations):
                temp = next_temp((i + 1) * (j + 1))
                heartrate = next_heartrate((i + 1) * (j + 1))
                lat, lon = next_geo2d((i + 1) * (j + 1), interval)

                startingTime = datetime.now().timestamp()

                intervalInSecs = (interval * 60) * j
                startingTime += intervalInSecs

                dt_object = datetime.fromtimestamp(startingTime)
                formatted_time = dt_object.strftime('%Y-%m-%d %H:%M:%S')

                new_datalog = DataLog(
                    id_animal_collar=new_animal_collar.id_animal_collar,
                    temperature=temp,
                    heartrate=heartrate,
                    latitude=lat,
                    longitude=lon,
                    created_at=formatted_time
                )
                session.add(new_datalog)
                session.commit()

        print("Farm populated successfully with:")
        print("1 species,")
        print("1 breed,")
        print(f"{animalNumber} animals,")
        print(f"{animalNumber} collars,")
        print(f"{animalNumber} animal-collar links.")
        print(f"{animalNumber * iterations} data logs.")
        
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    populate_db()
    #print("a")