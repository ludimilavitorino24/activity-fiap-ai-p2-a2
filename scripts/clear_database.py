import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from db import engine, DataLog, Species, Breed, Animal, Collar, AnimalCollar, Alert
from sqlalchemy.orm import sessionmaker

print("INFO: Cleaning database")

Session = sessionmaker(bind=engine)
session = Session()

session.query(Alert).delete()
session.query(DataLog).delete()
session.query(AnimalCollar).delete()
session.query(Collar).delete()
session.query(Animal).delete()
session.query(Breed).delete()
session.query(Species).delete()

session.commit()
session.close()

