import io
import pandas as pd
from influxdb_client_3 import InfluxDBClient3
import os

# Read environment variables
token = os.getenv('TOKEN')
database = os.getenv('DATABASE')
host = os.getenv('HOST')

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    client = InfluxDBClient3(token=token,
                         host=host,
                         org="89711f17730122e0",
                         database=database)
                         
    query = "SELECT * FROM \"cpu\" WHERE time >= now() - interval '10 minutes'AND \"cpu\" IN ('cpu-total')"
    data = client.query(query=query, language="sql", mode='pandas')

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
