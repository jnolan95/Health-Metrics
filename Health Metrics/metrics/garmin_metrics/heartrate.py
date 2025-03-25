from metrics.fitbit_metrics.fitbit_metric_class import GarminMetric
import garth
import pandas as pd

class Heartrate(GarminMetric):
    def __init__(self, calendar_data):
        super().__init__(calendar_data)
        self.gather_heartrate_data()


        #self.df = self.df[["Date", "Zone 2", "Zone 5"]]

    def gather_heartrate_data(self):
        self.heartrate_data = garth.DailyIntensityMinutes.list(self.calendar_end, self.calendar_range)
        self.df = pd.DataFrame(self.heartrate_data)


        #self.df["Date"] = self.df["calendar_date"]
        #self.df["Zone 2"] = self.df["moderate_value"]
        #self.df["Zone 5"] = self.df["vigorous_value"]

        #     DailyIntensityMinutes(
        #         calendar_date=datetime.date(2023, 7, 28),
        #         weekly_goal=150,
        #         moderate_value=0,
        #         vigorous_value=0
        #     ),
        #     DailyIntensityMinutes(
        #         calendar_date=datetime.date(2023, 7, 29),
        #         weekly_goal=150,
        #         moderate_value=0,
        #         vigorous_value=0
        #     )
        # ]

