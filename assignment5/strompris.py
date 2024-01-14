#!/usr/bin/env python3
"""
Fetch data from https://www.hvakosterstrommen.no/strompris-api
and visualize it.

Assignment 5
"""

import datetime
import warnings

import altair as alt
import pandas as pd
import requests
import requests_cache

# install an HTTP request cache
# to avoid unnecessary repeat requests for the same data
# this will create the file http_cache.sqlite
requests_cache.install_cache()

# suppress a warning with altair 4 and latest pandas
warnings.filterwarnings("ignore", ".*convert_dtype.*", FutureWarning)


# task 5.1:


def fetch_day_prices(date: datetime.date = None, location: str = "NO1") -> pd.DataFrame:
    """Fetch one day of data for one location from hvakosterstrommen.no API

    Arguments:
        date (datetime.date): the date to fetch prices for
        location (str): the location to fetch prices for

    Returns:
        pd.DataFrame: a data frame with the columns "time_start" and "NOK_per_kWh"
    """

    if date is None:
        date = datetime.date.today()

    year = date.strftime("%Y")
    month = date.strftime("%m")
    day = date.strftime("%d")

    url = f"https://www.hvakosterstrommen.no/api/v1/prices/{year}/{month}-{day}_{location}.json"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return pd.DataFrame()

    df = pd.DataFrame.from_dict(response.json())

    df["time_start"] = pd.to_datetime(df["time_start"], utc=True).dt.tz_convert(
        "Europe/Oslo"
    )

    df["NOK_per_kWh"] = df["NOK_per_kWh"].astype(float)

    return df


# LOCATION_CODES maps codes ("NO1") to names ("Oslo")
LOCATION_CODES = {
    "NO1": "Oslo",
    "NO2": "Kristiansand",
    "NO3": "Trondheim",
    "NO4": "Tromsø",
    "NO5": "Bergen",
}

# task 1:


def fetch_prices(
    end_date: datetime.date = None,
    days: int = 7,
    locations: list[str] = tuple(LOCATION_CODES.keys()),
) -> pd.DataFrame:
    """Fetch prices for multiple days and locations into a single DataFrame

    Arguments:
        end_date (datetime.date): the last date to fetch prices for
        days (int): the number of days to fetch prices for, but with no arguments, it should fetch the latest 7 days of data
        locations (list[str]): the locations to fetch prices for

    Returns:
        pd.DataFrame: a data frame with the columns "time_start", "location_code", "location", and "NOK_per_kWh"
    ...
    """

    if end_date is None:
        end_date = datetime.date.today()

    start_date = end_date - datetime.timedelta(days=days - 1)
    all_data = []

    for day_offset in range(days):
        current_date = start_date + datetime.timedelta(days=day_offset)
        for location_code in locations:
            daily_data = fetch_day_prices(date=current_date, location=location_code)
            daily_data["location_code"] = location_code
            location_name = LOCATION_CODES.get(location_code)
            daily_data["location"] = location_name
            all_data.append(daily_data)

    return pd.concat(all_data).reset_index(drop=True)


# task 5.1:


def plot_prices(df: pd.DataFrame) -> alt.Chart:
    """Plot energy prices over time

    Arguments:
        df (pd.DataFrame): a data frame with the columns "time_start", "location_code", "location", and "NOK_per_kWh"

    Returns:
        alt.Chart: an altair chart object
    """

    chart = (
        alt.Chart(df)
        .mark_line()
        .encode(
            x="time_start:T",
            y="NOK_per_kWh:Q",
            color="location:N",
        )
        .properties(title="Energy Prices over Time by Location")
    )

    return chart


# Task 5.4


def plot_daily_prices(df: pd.DataFrame) -> alt.Chart:
    """Plot the daily average price

    x-axis should be time_start (day resolution)
    y-axis should be price in NOK

    You may use any mark.

    Make sure to document arguments and return value...
    """
    raise NotImplementedError("Remove me when you implement this task (in4110 only)")
    ...


# Task 5.6

ACTIVITIES = {
    # activity name: energy cost in kW
    ...
}


def plot_activity_prices(
    df: pd.DataFrame, activity: str = "shower", minutes: float = 10
) -> alt.Chart:
    """
    Plot price for one activity by name,
    given a data frame of prices, and its duration in minutes.

    Make sure to document arguments and return value...
    """
    raise NotImplementedError("Remove me when you implement this optional task")

    ...


def main():
    """Allow running this module as a script for testing."""
    df = fetch_prices()
    chart = plot_prices(df)
    # showing the chart without requiring jupyter notebook or vs code for example
    # requires altair viewer: `pip install altair_viewer`
    chart.show()


if __name__ == "__main__":
    main()
