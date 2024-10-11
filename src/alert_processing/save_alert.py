from db import engine, Alert
from sqlalchemy.orm import sessionmaker
from typings import AlertMetric


def save_alert(
    alert_metric: AlertMetric,
    alert_type: str,
    id_datalog: int,
) -> None:
    """Save the alert to the database."""
    try:
        SessionLocal = sessionmaker(bind=engine)
        session = SessionLocal()

        existing_alert = (
            session.query(Alert)
            .filter_by(
                id_datalog=id_datalog, alert_metric=alert_metric, alert_type=alert_type
            )
            .first()
        )

        if existing_alert:
            return

        new_alert = Alert(
            id_datalog=id_datalog,
            alert_type=alert_type,
            alert_metric=alert_metric,
        )
        session.add(new_alert)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()
