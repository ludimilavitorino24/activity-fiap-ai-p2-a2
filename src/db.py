from sqlalchemy import (
    Column, Integer, String, Date, Numeric, ForeignKey, TIMESTAMP, Boolean,
    create_engine
)
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

import dotenv
dotenv.load_dotenv()
import os

DATABASE_URL = os.getenv("DB_URL")

engine = create_engine(DATABASE_URL)

# Base class for declarative model definitions
Base = declarative_base()

#region Models

Base = declarative_base()

# t_wc_species table
class Species(Base):
    __tablename__ = 't_wc_species'

    id_species = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

    animals = relationship('Animal', back_populates='species')


# t_wc_breeds table
class Breed(Base):
    __tablename__ = 't_wc_breeds'

    id_breed = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

    animals = relationship('Animal', back_populates='breed')


# t_wc_animals table
class Animal(Base):
    __tablename__ = 't_wc_animals'

    id_animal = Column(Integer, primary_key=True, autoincrement=True)
    tag_id = Column(Integer, nullable=False)
    name = Column(String(50), nullable=False)
    birth_date = Column(Date)
    id_species = Column(Integer, ForeignKey('t_wc_species.id_species'), nullable=False)
    id_breed = Column(Integer, ForeignKey('t_wc_breeds.id_breed'), nullable=False)
    is_deleted = Column(Boolean, nullable=False, default=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

    species = relationship('Species', back_populates='animals')
    breed = relationship('Breed', back_populates='animals')
    collars = relationship('AnimalCollar', back_populates='animal')


# t_wc_collars table
class Collar(Base):
    __tablename__ = 't_wc_collars'

    id_collar = Column(Integer, primary_key=True, autoincrement=True)
    is_deleted = Column(Boolean, nullable=False, default=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

    animal_collars = relationship('AnimalCollar', back_populates='collar')


# t_wc_animals_collars table
class AnimalCollar(Base):
    __tablename__ = 't_wc_animals_collars'

    id_animal_collar = Column(Integer, primary_key=True, autoincrement=True)
    id_collar = Column(Integer, ForeignKey('t_wc_collars.id_collar'), nullable=False)
    id_animal = Column(Integer, ForeignKey('t_wc_animals.id_animal'), nullable=False)
    is_deleted = Column(Boolean, nullable=False, default=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

    collar = relationship('Collar', back_populates='animal_collars')
    animal = relationship('Animal', back_populates='collars')
    datalog = relationship('DataLog', back_populates='animal_collar')


# t_wc_datalog table
class DataLog(Base):
    __tablename__ = 't_wc_datalog'

    id_datalog = Column(Integer, primary_key=True, autoincrement=True)
    id_animal_collar = Column(Integer, ForeignKey('t_wc_animals_collars.id_animal_collar'), nullable=False)
    temperature = Column(Numeric)
    heartrate = Column(Integer)
    latitude = Column(Numeric)
    longitude = Column(Numeric)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    is_outlier = Column(Boolean, nullable=False, default=False)

    animal_collar = relationship('AnimalCollar', back_populates='datalog')

#endregion

# Create the table(s) in the database
Base.metadata.create_all(engine)
