# Imports
import datetime

# Packages
import pandas
from nose.tools import assert_true, assert_equal, assert_in

# Project imports
from pyghcn.client import get_station_daily_data, get_station_list_data
from pyghcn.data import extract_series_from_daily_data, get_nearby_stations


def test_extract_series_from_daily_data_1():
    """
    Test extracting max temperature from DTW.
    :return:
    """
    # get and parse station data
    daily_df = get_station_daily_data("USW00094847")
    tmax_series = extract_series_from_daily_data("TMAX", daily_df)

    # check type, temp, and size
    assert_equal(type(tmax_series), pandas.Series)
    assert_equal(tmax_series.loc[datetime.date(2018, 6, 30)], 344)
    assert_true(tmax_series.shape[0] > 1000)

def test_get_nearby_stations_1():
    """
    Test extracting max temperature from DTW.
    :return:
    """
    # get and parse station data
    station_df = get_station_list_data()
    nearby_stations = get_nearby_stations(station_df, 40.5, -85.5, 10, "mi", "IN")

    # check type, temp, and size
    assert_in("US1INBL0003", nearby_stations)