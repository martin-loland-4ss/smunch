import os

import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = os.environ["API_URL"]


def generate_df():
    data = {"a": [1, 2, 3], "b": [4, 5, 6]}
    return pd.DataFrame(data)


def get_api_data():
    response = requests.get(API_URL)
    print(response.json())


get_api_data()
