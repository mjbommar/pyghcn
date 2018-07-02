"""The pyghcn.client module provides a low-level client to retrieve key data from GHCN over FTP or HTTP."""

# Imports
import io
import ftplib

# Packages
import requests
import pandas

# Project imports
from pyghcn.constants import FTP_HOST, HTTP_HOST, \
    VERSION_FILE_PATH, INVENTORY_FILE_PATH, STATION_FILE_PATH, \
    INVENTORY_FILE_COLUMNS, STATION_FILE_COLUMNS, DAILY_FILE_COLUMNS, \
    INVENTORY_FILE_DTYPES, STATION_FILE_DTYPES, DAILY_FILE_DTYPES, \
    INVENTORY_FILE_WIDTHS, STATION_FILE_WIDTHS, DAILY_FILE_WIDTHS


def get_buffer(path, protocol="ftp", ftp_connection=None):
    """
    Get a buffer at a given path using either FTP or HTTP.
    :param path: str, path to file to retrieve
    :param protocol: str, ftp or http to set protocol
    :param ftp_connection: ftplib.Connection, optional conn to re-use
    :return:
    """

    # Switch on method
    if protocol == "ftp":
        # Create IO buffer
        io_buffer = io.BytesIO()

        # Check if we're re-using a connection
        if not ftp_connection:
            with ftplib.FTP(FTP_HOST, user="anonymous", passwd="anonymous") as ftp_connection:
                ftp_connection.retrbinary("RETR {0}".format(path), io_buffer.write)
        else:
            ftp_connection.retrbinary("RETR {0}".format(path), io_buffer.write)

        # Reset position and return
        io_buffer.seek(0)
        return io_buffer
    elif protocol == "http":
        # Build URL
        http_url = "https://{0}/{1}".format(HTTP_HOST, path.lstrip("/"))

        # Get with requests
        r = requests.get(http_url)
        return io.BytesIO(r.content)


def get_ghcnd_version(protocol="ftp", ftp_connection=None):
    """
    Get GHCN-D version string.
    """
    # Create IO buffer
    version_response = get_buffer(VERSION_FILE_PATH, protocol, ftp_connection)

    # Parse version text and return string
    version_text = version_response.getvalue().decode('utf-8')
    p0 = version_text.find("GHCN Daily is") + len("GHCN Daily is") + 1
    p1 = version_text.find("(", p0)
    return version_text[p0:p1].strip()


def get_station_list_buffer(protocol="ftp", ftp_connection=None):
    """
    Get raw station file data as an io object.
    """
    # Call get_buffer and return
    station_list_buffer = get_buffer(STATION_FILE_PATH, protocol, ftp_connection)
    return station_list_buffer


def get_station_list_data(protocol="ftp", ftp_connection=None):
    """
    Get station list as pandas DataFrame.
    """
    # Get buffer
    station_buffer = get_station_list_buffer(protocol, ftp_connection)
    station_df = pandas.read_fwf(station_buffer, header=None, names=STATION_FILE_COLUMNS, dtypes=STATION_FILE_DTYPES,
                                 widths=STATION_FILE_WIDTHS)
    return station_df


def get_station_inventory_buffer(protocol="ftp", ftp_connection=None):
    """
    Get raw station inventory data as an io object.
    """
    # Call get_buffer and return
    station_inventory_buffer = get_buffer(INVENTORY_FILE_PATH, protocol, ftp_connection)
    return station_inventory_buffer


def get_station_inventory_data(protocol="ftp", ftp_connection=None):
    """
    Get station inventory as pandas DataFrame.
    """
    # Get buffer
    inventory_buffer = get_station_inventory_buffer(protocol, ftp_connection)
    inventory_df = pandas.read_fwf(inventory_buffer, header=None, names=INVENTORY_FILE_COLUMNS,
                                   dtypes=INVENTORY_FILE_DTYPES,
                                   widths=INVENTORY_FILE_WIDTHS)
    return inventory_df


def get_station_daily_path(station_id):
    """
    Get path to a station daily file.
    :param station_id:
    :return:
    """
    return "/pub/data/ghcn/daily/all/{0}.dly".format(station_id)


def get_station_daily_buffer(station_id, protocol="ftp", ftp_connection=None):
    """
    Get raw station daily buffer as an io object.
    :param station_id: str, station ID
    :param protocol: str, ftp or http
    :param ftp_connection: ftplib.Connection, optional conn to reuse
    :return:
    """
    # Call get_buffer and return
    station_daily_buffer = get_buffer(get_station_daily_path(station_id), protocol, ftp_connection)
    return station_daily_buffer


def get_station_daily_data(station_id, protocol="ftp", ftp_connection=None):
    """
    Get station inventory as pandas DataFrame.
    """
    # Get buffer
    station_daily_buffer = get_station_daily_buffer(station_id, protocol, ftp_connection)
    station_daily_df = pandas.read_fwf(station_daily_buffer, header=None, names=DAILY_FILE_COLUMNS,
                                       dtypes=DAILY_FILE_DTYPES,
                                       widths=DAILY_FILE_WIDTHS)
    return station_daily_df
