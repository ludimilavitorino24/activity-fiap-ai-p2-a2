import pandas as pd

from alert_processing.fetch_data import fetch_data
from alert_processing.save_alert import save_alert


def z_score(series: pd.Series):
    return (series - series.mean()) / series.std()


def getALertDict(alerts_df: pd.DataFrame) -> dict:
    assert (
        "alert_type" in alerts_df.columns
    ), "DataFrame must contain 'alert_type' column"
    assert (
        "alert_metric" in alerts_df.columns
    ), "DataFrame must contain 'alert_metric' column"

    alerts = []
    for i, row in alerts_df.iterrows():
        alerts.append(
            {
                "id_datalog": row["id_datalog"],
                "id_animal": row["id_animal"],
                "id_animal_collar": row["id_animal_collar"],
                "alert_metric": row["alert_metric"],
                "alert_type": row["alert_type"],
            }
        )

    return alerts


def process_temperature(data, threshold: float = 1.7):
    temperatures = data["temperature"]
    temperatures_z = z_score(temperatures)

    z_outliers_above_indices = temperatures_z >= threshold
    z_outliers_below_indices = temperatures_z <= -threshold

    data_outliers_above = data[z_outliers_above_indices].copy()
    data_outliers_below = data[z_outliers_below_indices].copy()

    data_outliers_above["alert_metric"] = "temperature"
    data_outliers_below["alert_metric"] = "temperature"

    data_outliers_above["alert_type"] = "z_score_outlier_above"
    data_outliers_below["alert_type"] = "z_score_outlier_below"
    
    data_temperature = pd.concat([data_outliers_above, data_outliers_below]).sort_index()

    return getALertDict(data_temperature)


def process_heartrate(data):
    return data


def process_movement(data):
    return data


def process_alerts(day: str):
    data = fetch_data(day)

    temperature_alerts = process_temperature(data)

    for alert in temperature_alerts:
        save_alert(**alert)

    # heart_rate_alerts = process_heartrate(data)

    # for alert in heart_rate_alerts:
    #     save_alert("heartrate", id_animal_collar, id_animal, id_data_log)

    # movement_alerts = process_movement(data)

    # for alert in movement_alerts:
    #     save_alert("movement", id_animal_collar, id_animal, id_data_log)
