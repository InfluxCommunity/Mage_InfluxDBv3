import pandas as pd
from influxdb_client_3 import InfluxDBClient3
import os

# Read environment variables
token = os.getenv('TOKEN')
database = os.getenv('DATABASE')
host = os.getenv('HOST')

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(data, *args, **kwargs):
    """
    Exports data to some source.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Output (optional):
        Optionally return any object and it'll be logged and
        displayed when inspecting the block run.
    """
    client = InfluxDBClient3(token=token,
                        host=host,
                        org="",
                        database=database)

    client.write(data, data_frame_measurement_name='cpu_avg')


