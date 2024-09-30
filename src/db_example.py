## Example: Query all animals from the database

import main
from db import engine, Animal
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

animals = session.query(Animal).all()

for animal in animals:
    print(animal)

session.close()
