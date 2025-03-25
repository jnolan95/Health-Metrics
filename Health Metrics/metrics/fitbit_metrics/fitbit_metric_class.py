from login_files.fitbit_login_files import fitbit_class
import pandas as pd

class Metric:
    def __init__(self, calendar_data):
        self.calendar_start = calendar_data["calendar_start"]
        self.calendar_end = calendar_data["calendar_end"]
        self.calendar_range = calendar_data["calendar_range"]
        self.calendar_range_list = calendar_data["calendar_range_list"]


class FitbitMetric(Metric):
    def __init__(self, calendar_data):
        super().__init__(calendar_data)
        self.contact_api = fitbit_class.fitbit.time_series(resource=self.resource, base_date=self.calendar_start, end_date=self.calendar_end)
        self.resource = self.resource.replace("/", "-")
        self.df = pd.DataFrame(self.contact_api[self.resource])

        # Uncomment these for Date
        self.df = self.df.rename(columns={"dateTime": "Date"})
        self.df["Date"] = self.convert_to_datetime()

    def convert_to_datetime(self):
        input = self.contact_api[self.resource]
        date_list = []
        for i in range(len(input)):
            date_list.append(pd.to_datetime(input[i]["dateTime"]).date())
        return date_list





class GarminMetric(Metric):
    def __init__(self, calendar_data):
        super().__init__(calendar_data)
