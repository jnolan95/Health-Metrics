from calendar_logic import get_month_calendar_data, get_week_calendar_data, get_custom_calendar_data
from metrics.fitbit_metrics.water import Water
import pandas as pd
from analysis.sleep_analysis import run_sleep_analysis, run_sleep_analysis2

from metrics.fitbit_metrics.body import BodyWeight, BodyFat
from metrics.garmin_metrics.sleep import Sleep
from metrics.garmin_metrics.heartrate import Heartrate
from metrics.garmin_metrics.steps import Steps


# Make class Report that can then be used for Weekly, Monthly, or (eventually) a variable duration for a report. 
# Gathers dataframes from all metrics and runs method create_data_frame to make a master dataframe of all data.
# Resulting DataFrame has a multitude of uses but is conveninent to have all information formatted and in one place.
class Report:
    def __init__(self, calendar_data):
        self.water = Water(calendar_data)
        self.sleep = Sleep(calendar_data)
        self.bodyweight = BodyWeight(calendar_data)
        #self.bodyfat = BodyFat(calendar_data)
        #self.heartrate = Heartrate(calendar_data)
        #self.steps = Steps(calendar_data)




        self.df = pd.DataFrame(calendar_data["calendar_range_list"], columns=["Date"])
        #print(self.steps.df)

        self.create_data_frame(calendar_data["calendar_range_list"])



        run_sleep_analysis(self.sleep.sleep_data)
        run_sleep_analysis2(self.sleep.sleep_data)
        print(self.df)

    # Creates a DataFrame, using METRIC_LIST (a master list of all current metrics)
    # Method has input of calendar_range_list so that we can set a standard/consistent for the dates
    # For loop after iterates through METRIC_LIST, merging the DataFrame associated with the Metric to the Main DataFrame, based "on" the date
    def create_data_frame(self, calendar_range_list):
        resource = self.sleep.__class__.__name__
        #self.metric_df = self.sleep.df.to_csv(f'/Users/johnnolan/Desktop/df_files/{resource}', index=False)
        self.METRIC_LIST = (self.water.df, self.sleep.df, self.bodyweight.df)
        self.df = pd.DataFrame(calendar_range_list, columns=["Date"])
        for df in self.METRIC_LIST:
            #resource = df.__class__.__name__
            #self.metric_df = df.df.to_csv(f'/Users/johnnolan/Desktop/df_files/{resource}', index=False)
            self.df = pd.merge(self.df, df, on="Date", how="outer")



# This is what is called in the main function. Class Monthly Report with SuperClass Report.
class MonthlyReport(Report):
    def __init__(self):
        self.calendar_data = get_month_calendar_data()
        super().__init__(self.calendar_data)


    # def generate_monthly_report(self):
    #     pass

# Same as Monthly Report. 
class WeeklyReport(Report):
    def __init__(self):
        self.calendar_data = get_week_calendar_data()
        super().__init__(self.calendar_data)


    # def generate_weekly_report(self):
    #     pass

#  Potential to build out later.
class YearlyReport(Report):
    def __init__(self):
        self.calendar_data = {}

class CustomReport(Report):
    def __init__(self):
        self.calendar_data = get_custom_calendar_data()
        super().__init__(self.calendar_data)