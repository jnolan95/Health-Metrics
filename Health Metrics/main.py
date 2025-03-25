from report_class import WeeklyReport, MonthlyReport, CustomReport
from login_files import login_checker

# Checks login credentials for both Garmin and Fitbit. If either's token has expired, will ask user for credentials or redirect to website.
# Gets booleans from calendar_logic to assess whether or not a report is due based on the last one that was run.
# The purpose behind this is that in due time the process could be automated and maybe the DataFrames are saved somewhere for weekly/monthly analysis.
def main():
    login_checker.check_login()
    # Generates weekly report if one is "due" (means at a minimum a week has elapsed since the last Weekly Report)
    print("Weekly Report:")
    weekly_report = WeeklyReport()
    # Same as above except for a month. e.g: It is March 1st. calendar_logic recognizes the last report was run sometime in February for the month of January and as such a report is due.
    print("Monthly Report:")
    monthly_report = MonthlyReport()
    #custom_report = CustomReport()




if __name__ == "__main__":
    main()