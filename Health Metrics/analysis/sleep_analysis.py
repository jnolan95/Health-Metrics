import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def run_sleep_analysis(sleep_data):
    df = pd.DataFrame(sleep_data)

    df["deep_sleep_hours"] = (
        df["deep_sleep_seconds"] / 3600
    )
    df["light_sleep_hours"] = (
        df["light_sleep_seconds"] / 3600
    )
    df["rem_sleep_hours"] = (
        df["rem_sleep_seconds"] / 3600
    )
    df["awake_sleep_hours"] = (
        df["awake_sleep_seconds"] / 3600
    )
    df["calendar_date"] = (
        pd.to_datetime(df["calendar_date"]).dt.date
    )

    df.sort_values("calendar_date", inplace=True)
    df.set_index("calendar_date", inplace=True)
    df.rename(columns={
        "deep_sleep_hours": "Deep",
        "light_sleep_hours": "Light",
        "rem_sleep_hours": "REM",
        "awake_sleep_hours": "Awake"
    }, inplace=True)

    sns.set_theme()

    ax = df[["Deep", "Light", "REM", "Awake"]].plot(
        kind="bar", stacked=True, figsize=(10, 6), grid=True, colormap="viridis",
        width=1
    )

    plt.ylabel("Hours")
    plt.xlabel(None)
    plt.title("Daily Sleep Stages")
    plt.grid(axis="x")
    plt.legend(loc="upper left")
    labels = ax.get_xticklabels()
    ticks = ax.get_xticks()
    ax.set_xticks([tick for i, tick in enumerate(ticks) if i % 4 == 0])
    ax.set_xticklabels([label for i, label in enumerate(labels) if i % 4 == 0])
    plt.xticks(rotation=45, ha="right")

    plt.show()

def run_sleep_analysis2(sleep_data):
    df = pd.DataFrame(sleep_data)
    df.sort_values("calendar_date", inplace=True)
    df.set_index("calendar_date", inplace=True)

    # Convert index to datetime
    df.index = pd.to_datetime(df.index)

    # Get the provided timestamp columns (in milliseconds)
    start_col = "sleep_start_timestamp_local"
    end_col = "sleep_end_timestamp_local"

    # Convert the timestamps (in milliseconds) to hours and minutes
    df["sleep_start_time"] = pd.to_datetime(df[start_col], unit="ms").dt.time
    df["sleep_end_time"] = pd.to_datetime(df[end_col], unit="ms").dt.time

    # Convert time to hours, with 18:00 as the starting point
    def convert_time(time_obj):
        hours_from_6 = time_obj.hour + time_obj.minute / 60 - 6
        return hours_from_6 if hours_from_6 >= 0 else hours_from_6 + 24

    df["sleep_start_hours"] = df["sleep_start_time"].apply(convert_time)
    df["sleep_end_hours"] = df["sleep_end_time"].apply(convert_time)

    # Plot
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x=df.index, y="sleep_start_hours", label="Sleep Start", marker="o")
    sns.lineplot(data=df, x=df.index, y="sleep_end_hours", label="Sleep End", marker="o")

    # Formatting
    plt.title("Sleep Start and End Time")
    plt.ylabel("Time of Day")
    plt.xlabel("Date")
    plt.grid(axis="x")
    plt.xticks(df.index[::4], rotation=45, ha="right")
    plt.yticks(range(0, 16, 2), [f"{(h + 6) % 24:02d}:00" for h in range(0, 16, 2)])
    plt.ylim(0, 16)
    plt.tight_layout()
    plt.legend()
    plt.show()