## Consultando

# O script `db_example.py` demonstra como consultar dados de um banco de dados, como animais.

# Para executar este script, siga estas etapas:

# 1. Execute o script executando o comando `python src/db_example.py`.
# 2. O script se conectará ao banco de dados e recuperará os dados dos animais com base na consulta fornecida.
# 3. Os dados dos animais consultados serão exibidos no console.

# Observação: Este script pode ser usado como referência para consultar qualquer tipo de dado de um banco de dados.

## Exemplo: Consultar todos os animais do banco de dados

import main
from db import engine, Animal
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

animals = session.query(Animal).all()

for animal in animals:
    print(animal)

session.close()
