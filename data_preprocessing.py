# author: Lynn Wu
# date: 2021-11-23

"""Preprocess data from the downloaded csv data.
Usage: data_preprocessing.py [--url=<url>] [--outputfile=<outputfile>]
Options:
[--inputfile=<inputfile>]       Input path where the data is saved locally.
[--outputfile=<outputfile>]     Output path to save the preprocessed data locally.
"""

import os
import pandas as pd
import requests
from sklearn.preprocessing import (
    OneHotEncoder,
    StandardScaler
)

from docopt import docopt
import traceback
import logging as logger
import sys

# from utils.util import get_config

