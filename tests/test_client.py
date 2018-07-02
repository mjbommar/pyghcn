# Imports
from nose.tools import assert_equal, assert_true

# Project imports
from pyghcn.client import get_ghcnd_version, get_station_list_data, get_station_daily_data


def test_get_ghcnd_version_ftp():
    """
    Test version string
    :return:
    """
    # Check that we start with 3...
    version_string = get_ghcnd_version()
    assert_equal(version_string[0], "3")


def test_get_ghcnd_version_http():
    """
    Test version string
    :return:
    """
    # Check that we start with 3...
    version_string = get_ghcnd_version()
    assert_equal(version_string[0], "3")


def test_get_station_list_data_ftp():
    """
    Test station list over FTP
    :return:
    """
    station_df = get_station_list_data(protocol="ftp")
    assert_true(station_df.shape[0] > 100000)
    assert_equal(station_df.shape[1], 9)
    assert_equal(station_df.columns[0], "STATION_ID")


def test_get_station_list_data_http():
    """
    Test station list over HTTP
    :return:
    """
    station_df = get_station_list_data(protocol="http")
    assert_true(station_df.shape[0] > 100000)
    assert_equal(station_df.shape[1], 9)
    assert_equal(station_df.columns[0], "STATION_ID")


def test_get_station_daily_data_ftp():
    """
    Test daily station data with FTP
    :return:
    """
    daily_station_df = get_station_daily_data("USW00094847", protocol="ftp")
    assert_true(daily_station_df.shape[0] > 14000)
    assert_equal(daily_station_df.shape[1], 128)
    assert_equal(daily_station_df.columns[0], "ID")


def test_get_station_daily_data_http():
    """
    Test daily station data with FTP
    :return:
    """
    daily_station_df = get_station_daily_data("USW00094847", protocol="http")
    assert_true(daily_station_df.shape[0] > 14000)
    assert_equal(daily_station_df.shape[1], 128)
    assert_equal(daily_station_df.columns[0], "ID")
