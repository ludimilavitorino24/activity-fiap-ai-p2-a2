import pandas as pd

from alert_processing.fetch_data import fetch_data


def z_score(series: pd.Series):
    return (series - series.mean()) / series.std()


def process_temperature(data, threshould: float = 1.5):
    temperatures = data["temperature"]
    temperatures_z = z_score(temperatures)
    print(temperatures_z)

    positive_outliers = temperatures_z >= threshould
    negative_outliers = temperatures_z <= -threshould

    print(positive_outliers)
    print(negative_outliers)

    outliers = temperatures_z[
        (temperatures_z >= threshould) | (temperatures_z <= -threshould)
    ]
    outliers_index = outliers.index
    print(outliers_index)

    return data[data.index.isin(outliers_index)]


def process_heartrate(data):
    return data


def process_movement(data):
    return data


def process_alerts(day: str):
    data = fetch_data(day)

    temperature_alerts = process_temperature(data)
    
    print(temperature_alerts)
    assert False

    for alert in temperature_alerts:
        save_alert("temperature", id_animal_collar, id_animal, id_data_log)

    heart_rate_alerts = process_heartrate(data)

    for alert in heart_rate_alerts:
        save_alert("heartrate", id_animal_collar, id_animal, id_data_log)

    movement_alerts = process_movement(data)

    for alert in movement_alerts:
        save_alert("movement", id_animal_collar, id_animal, id_data_log)
