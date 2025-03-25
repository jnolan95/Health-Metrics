import garth
import pandas as pd
import datetime
from metrics.fitbit_metrics.fitbit_metric_class import GarminMetric
from login_files.garmin_login_files.garmin_login_resume import resume_session

# replace latest with the date of the last day of the month/ week

# replace RANGE with the length of the month

class Sleep(GarminMetric):
    def __init__(self, calendar_data):
        super().__init__(calendar_data)
        self.gather_sleep_data()
        self.sleep_start_end_duration()
        self.df = self.df[["Date", "Sleep Start", "Sleep End", "Sleep Duration"]]




    def gather_sleep_data(self):
        self.sleep_data = [sd.daily_sleep_dto for sd in garth.SleepData.list(self.calendar_end, self.calendar_range)]
        self.df = pd.DataFrame(self.sleep_data)
        self.df["Date"] = self.df["calendar_date"]



    def sleep_start_end_duration(self):
        # self.df = self.df[self.df["Date"].isin(self.calendar_range_list)]
        self.df["Sleep Start"] = pd.to_datetime(self.df['sleep_start_timestamp_local'], unit="ms")
        self.df['Sleep Start'] = self.df['Sleep Start'].dt.strftime('%H:%M')
        self.df["Sleep End"] = pd.to_datetime(self.df['sleep_end_timestamp_local'], unit="ms")
        self.df["Sleep End"] = self.df["Sleep End"].dt.strftime('%H:%M')
        self.df["Sleep Duration"] = pd.to_datetime(self.df["sleep_time_seconds"], unit="s").dt.time

