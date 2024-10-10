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


def process_outliers(data, field_name: str, threshold: float = 1.7):
    field_data = data[field_name]
    field_z = z_score(field_data)

    z_outliers_above_indices = field_z >= threshold
    z_outliers_below_indices = field_z <= -threshold

    data_outliers_above = data[z_outliers_above_indices].copy()
    data_outliers_below = data[z_outliers_below_indices].copy()

    data_outliers_above["alert_metric"] = field_name
    data_outliers_below["alert_metric"] = field_name

    data_outliers_above["alert_type"] = "z_score_outlier_above"
    data_outliers_below["alert_type"] = "z_score_outlier_below"

    data_outliers = pd.concat([data_outliers_above, data_outliers_below]).sort_index()

    return getALertDict(data_outliers)


def process_alerts(day: str):
    data = fetch_data(day)

    temperature_alerts = process_outliers(data, "temperature", threshold=1.75)
    print(len(temperature_alerts))

    # for alert in temperature_alerts:
    #     save_alert(**alert)

    heart_rate_alerts = process_outliers(data, "heartrate", threshold=1.697)
    print(len(heart_rate_alerts))

    # for alert in heart_rate_alerts:
    #     save_alert(**alert)

    movement_alerts = process_outliers(data, "animal_distance_traveled", threshold=2.2)
    print(len(movement_alerts))

    # for alert in movement_alerts:
    #     save_alert(**alert)
