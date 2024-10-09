from db import engine, Alert
from sqlalchemy.orm import sessionmaker
from typings import AlertType

def save_alert(
    alert_type: AlertType,
    id_animal_collar: int,
    id_animal: int,
    id_data_log: int,
) -> None:
    """Save the alert to the database."""
    
    try:
        SessionLocal = sessionmaker(bind=engine)
        session = SessionLocal()

        new_alert = Alert(
            id_animal_collar = id_animal_collar,
            id_animal = id_animal,
            id_data_log = id_data_log,
            alert_type = alert_type
        )
        session.add(new_alert)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()