from typing import Literal

AlertMetric = Literal['temperature', 'heartrate', 'movement']

OutlierAlertType = Literal['z_score_outlier_above', 'z_score_outlier_below']