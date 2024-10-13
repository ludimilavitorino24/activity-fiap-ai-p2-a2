from typing import Literal, List

AlertMetric = Literal['temperature', 'heartrate', 'movement']

OutlierAlertType = Literal['z_score_outlier_above', 'z_score_outlier_below']

class ReportData:
    def __init__(self, name: str, breed: str, total_quantity: int, average_temperature: float, 
                 max_temperature: float, min_temperature: float, total_distance: float, 
                 average_distance: float, max_distance: float, min_distance: float):
        self.name = name
        self.breed = breed
        self.total_quantity = total_quantity
        self.average_temperature = average_temperature
        self.max_temperature = max_temperature
        self.min_temperature = min_temperature
        self.total_distance = total_distance
        self.average_distance = average_distance
        self.max_distance = max_distance
        self.min_distance = min_distance

class Report:
    def __init__(self, date: str, species: List[ReportData]):
        self.date = date
        self.species = species
