import garth
import pandas as pd
import datetime
from metrics.fitbit_metrics.fitbit_metric_class import GarminMetric
from login_files.garmin_login_files.garmin_login_resume import resume_session



class Steps(GarminMetric):
    def __init__(self, calendar_data):
        super().__init__(calendar_data)
        self.gather_steps_data()



    def gather_steps_data(self):
        self.steps_data = garth.DailySteps.list(self.calendar_end, self.calendar_range)
        self.df = pd.DataFrame(self.steps_data)
        self.df.drop(columns=['step_goal', "total_distance"], inplace=True)