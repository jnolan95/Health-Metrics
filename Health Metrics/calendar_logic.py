import datetime
from datetime import date
import json
import calendar
import pandas as pd

# The purpose of this code is to get the current date information and check it to
# see if a Monthly or Weekly Report is due.

# If you'd like to change the start of the week from Sunday to Monday, go the get_current_date and comment/uncomment


def main():
    date_info = get_current_date()
    return check_last_report(week_number=date_info[0], month=date_info[1])


def get_current_date():
    today = date.today()
    month = today.month

    # week number if Monday should be considered the start of the week
    # week_number = date(year=today.year, month=today.month, day=today.day).isocalendar().week

    # week number if Sunday should be considered the start of the week
    week_number = int(today.strftime("%U"))

    return week_number, month

# Checks JSON file and compares current week and month to see if a report is "due"
# For example: If it's the first of the month or a Sunday, a report would be due.
# After it is determined a report is due, return list with True or False if a week or month report is due.
# Example: [True, True] would indicate a Week Report and Month Report are due.
# Example: [False, True] would indicate only a Month Report is due
# If returning True, update the JSON file.


def check_last_report(week_number, month):
    with open("current_report.json") as json_file:
        data = json.load(json_file)

    last_week_number = data["week_number"]
    last_month = data["month"]

    reports_due = []
    if week_number > last_week_number or (week_number == 2 and (last_week_number == 52 or last_week_number == 53)):
        reports_due.append(True)
        update_memory(data, week_number=last_week_number + 1)
    else:
        reports_due.append(False)
    if month > last_month + 1 or (month == 2 and last_month == 12):
        reports_due.append(True)
        update_memory(data, month= last_month + 1)
    else:
        reports_due.append(False)
    return reports_due


def get_month_calendar_data():
    with open("current_report.json") as json_file:
        data = json.load(json_file)

    year = 2024
    if data["month"] == 12:
        month = 1
    else:
        month = data["month"]

    last_day_of_month = calendar.monthrange(year, month)[1]

    month_start = f"{year}-{month:02d}-01"
    month_end = f"{year}-{month:02d}-{last_day_of_month}"
    month_range = last_day_of_month - 1


    _, num_days = calendar.monthrange(year, month)
    month_range_list = [datetime.date(year, month, day) for day in range(1, num_days + 1)]
    for date in month_range_list:
        pd.to_datetime(date).date()

    return {"calendar_start": month_start, "calendar_end": month_end, "calendar_range": month_range, "calendar_range_list": month_range_list}



def get_week_calendar_data():
    with open("current_report.json") as json_file:
        data = json.load(json_file)

    # Get the first day of the week (Sunday)
    week_start = datetime.datetime.strptime(f'{data["year"]}-W{data["week_number"]}-0', "%G-W%V-%w").date()

    # Calculate the last day of the week (Saturday)
    week_end = week_start + datetime.timedelta(days=6)

    # first_day = datetime.datetime.strptime(f'{year}-W{week_number}-0', "%G-W%V-%w").date()

    # Calculate the rest of the days in the week
    week_range_list = [(week_start + datetime.timedelta(days=i)) for i in range(7)]

    for date in week_range_list:
        pd.to_datetime(date).date()

    return {"calendar_start": week_start, "calendar_end": week_end, "calendar_range": 7, "calendar_range_list": week_range_list}

def get_custom_calendar_data():
    date_start = input("Start date? ")
    date_end = input("End date? ")

    start_date = datetime.datetime.strptime(date_start, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(date_end, "%Y-%m-%d")

    delta = (end_date - start_date)
    date_range = delta.days


    date_range_list = [start_date + datetime.timedelta(days=i) for i in range(date_range + 1)]

    return {"calendar_start": date_start, "calendar_end": date_end, "calendar_range": date_range,
            "calendar_range_list": date_range_list}





# Conditional that updates JSON file, current_report.json, if a report is going to be created.
def update_memory(data, week_number=0, month=0, year=0):
    current_week = get_current_date()[0]
    current_month = get_current_date()[1]
    if week_number != 0:
        data["week_number"] = current_week - 1
    if month != 0:
        data["month"] = current_month - 1
    # if year != 0:
    #     data["year"] = year - 1


    with open("current_report.json", "w") as json_file:
        json.dump(data, json_file, indent=4)



if __name__ == "__main__":
    main()
