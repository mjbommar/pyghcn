"""The pyghcn.data module provides a high-level interface to extract data from GHCN for storage or analysis."""

# Imports
import datetime

# Packages
import pandas
import geopy.distance

# Project imports
from pyghcn.constants import DAILY_FILE_COLUMNS


def extract_series_from_daily_data(element, station_daily_df):
    """
    Extract a series for a given element from a daily station dataframe.
    :param element: str, ELEMENT value to filter by, e.g., TMIN or TMAX
    :param station_daily_df: pandas.DataFrame, input daily station file dataframe
    :return:
    """
    # Initialize return structure
    series_index = []
    series_rows = []

    # Iterate through subset rows
    for row_id, row in station_daily_df.loc[station_daily_df["ELEMENT"] == element].iterrows():
        for column_name in DAILY_FILE_COLUMNS:
            if column_name.startswith("VALUE"):
                # assume success in creating date
                try:
                    # get day from column name
                    row_date = datetime.date(row["YEAR"], row["MONTH"], int(column_name[5:]))
                except ValueError as e:
                    continue

                # append record
                series_index.append(row_date)
                series_rows.append(row[column_name])

    return pandas.Series(series_rows, index=series_index)


def get_nearby_stations(station_df, latitude, longitude, radius, unit="km", state=None):
    """
    Get nearby stations from a given lat,lon pair with a radius in units.  Optionally filter by GHCN STATE code
    for speedup.
    :param station_df: pandas.DataFrame, search dataframe list
    :param latitude: float, latitude
    :param longitude: float, longitude
    :param radius: float, radius in units
    :param unit: str, km, mi, nm
    :param state: str, optional filter for GHCN STATE code
    :return:
    """
    # Initialize return structure
    nearby_stations = []

    # Subset search dataframe if filtered by STATE
    if state is not None:
        search_df = station_df.loc[station_df["STATE"] == state]
    else:
        search_df = station_df

    # Search
    for row_id, row in search_df.iterrows():
        station_distance = geopy.distance.geodesic((latitude, longitude), (row["LATITUDE"], row["LONGITUDE"]))
        if unit == "km" and station_distance.km <= radius:
            nearby_stations.append(row["STATION_ID"])
        elif unit == "mi" and station_distance.mi <= radius:
            nearby_stations.append(row["STATION_ID"])
        elif unit == "nm" and station_distance.nm <= radius:
            nearby_stations.append(row["STATION_ID"])

    return nearby_stations
