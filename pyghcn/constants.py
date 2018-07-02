"""The pyghcn.constants module provides constant definition for use across other modules, including file format specs
and paths."""

# Connection data for HTTP and FTP
FTP_HOST = "ftp.ncdc.noaa.gov"
FTP_GCHN_PATH = "/pub/data/ghcn/"
HTTP_HOST = "www1.ncdc.noaa.gov"
HTTP_GCHN_PATH = "/pub/data/ghcn/"

# Key file paths
STATION_FILE_PATH = "/pub/data/ghcn/daily/ghcnd-stations.txt"
VERSION_FILE_PATH = "/pub/data/ghcn/daily/ghcnd-version.txt"
INVENTORY_FILE_PATH = "/pub/data/ghcn/daily/ghcnd-inventory.txt"

# File specifications
# Station file constants
STATION_FILE_DTYPES = {'STATION_ID': str,
                       'LATITUDE': str,
                       'LONGITUDE': str,
                       'ELEVATION': str,
                       'STATE': str,
                       'STATION_NAME': str,
                       'GSN_FLAG': str,
                       'HCN_CRN_FLAG': str,
                       'WMO_ID': str}

STATION_FILE_COLUMNS = ['STATION_ID', 'LATITUDE', 'LONGITUDE',
                        'ELEVATION', 'STATE', 'STATION_NAME',
                        'GSN_FLAG', 'HCN_CRN_FLAG', 'WMO_ID']

STATION_FILE_WIDTHS = [11,  # Station ID
                       9,  # Latitude (decimal degrees)
                       10,  # Longitude (decimal degrees)
                       7,  # Elevation (meters)
                       3,  # State (USA stations only)
                       31,  # Station Name
                       4,  # GSN Flag
                       4,  # HCN/CRN Flag
                       6]  # WMO ID

# Inventory file constants
INVENTORY_FILE_DTYPES = {"ID": str,
                         "LATITUDE": float,
                         "LONGITUDE": float,
                         "ELEMENT": str,
                         "FIRSTYEAR": int,
                         "LASTYEAR": int
                         }

INVENTORY_FILE_WIDTHS = [11,  # ID
                         10,  # LATITUDE
                         10,  # LONGITUDE
                         4,  # ELEMENT
                         5,  # FIRSTYEAR,
                         5,  # LASTYEAR
                         ]

INVENTORY_FILE_COLUMNS = ["ID", "LATITUDE", "LONGITUDE", "ELEMENT",
                          "FIRSTYEAR", "LASTYEAR"]

# Daily file constants
DAILY_FILE_DTYPES = {"ID": str,
                     "YEAR": int,
                     "MONTH": int,
                     "ELEMENT": str,
                     }
DAILY_FILE_WIDTHS = [11,  # ID
                     4,  # YEAR
                     2,  # MONTH
                     4,  # ELEMENT
                     ]
DAILY_FILE_COLUMNS = ["ID", "YEAR", "MONTH", "ELEMENT"]

base_pos = 21
for i in range(1, 32):
    # Dtypes
    DAILY_FILE_DTYPES["VALUE{0}".format(i)] = "int"
    DAILY_FILE_DTYPES["MFLAG{0}".format(i)] = "str"
    DAILY_FILE_DTYPES["QFLAG{0}".format(i)] = "str"
    DAILY_FILE_DTYPES["SFLAG{0}".format(i)] = "str"
    # Widths
    DAILY_FILE_WIDTHS.append(5)
    DAILY_FILE_WIDTHS.append(1)
    DAILY_FILE_WIDTHS.append(1)
    DAILY_FILE_WIDTHS.append(1)
    # Names
    DAILY_FILE_COLUMNS.append("VALUE{0}".format(i))
    DAILY_FILE_COLUMNS.append("MFLAG{0}".format(i))
    DAILY_FILE_COLUMNS.append("QFLAG{0}".format(i))
    DAILY_FILE_COLUMNS.append("SFLAG{0}".format(i))
