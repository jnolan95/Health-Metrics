from login_files.fitbit_login_files import fitbit_class
import pandas as pd
from datetime import datetime

from metrics.fitbit_metrics.fitbit_metric_class import FitbitMetric


class Water(FitbitMetric):
    def __init__(self, calendar_data):
        self.resource = "foods/log/water"
        super().__init__(calendar_data)
        self.df = self.df.rename(columns={"value": "Water"})
        self.df["Water"] = [int(float(volume)) for volume in self.df["Water"]]


