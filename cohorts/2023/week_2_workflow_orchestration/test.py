# Import necessary packages to create a DAG from Airflow ingesting data from a website and storing it in S3
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.decorators import task, dag
from datetime import datetime, timedelta
import requests
import pandas as pd
import logging
from pathlib import Path
import io
import boto3
from botocore.exceptions import NoCredentialsError
from io import BytesIO



# Define default arguments for the DAG
default_args = {
    "owner": "gluonhiggs",
    "depends_on_past": False,
    "start_date": datetime(2023, 5, 8),
    "email": ["love.fiziks@gmail.com"],
    "email_on_failure": True,
    "email_on_retry": True,
    "retries": 1,
    "retry_delay": timedelta(seconds=30)
}
schedule = timedelta(seconds=60)
description = "A simple DAG to ingest data from a website and store it in S3"




# Define the DAG with dag decorator
color = "green"
year = 2020
month = 1
dataset_filename = f"{color}_tripdata_{year}-{month:02d}.csv.gz"
dataset_url = f"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{color}/{dataset_filename}"
s3_url = f"s3://terraform-data-lake-666243375423.us-east-1/data/{color}_tripdata_2020-01.parquet.gzip"
s3_url = s3_url.replace("s3://", "s3a://")


def fetch_data(dataset_url:str)->pd.DataFrame:
    """
    Fetch data from a website
    """
    response = requests.get(dataset_url)
    if response.status_code == 200:
        df = pd.read_csv(dataset_url)
        return df
    else:
        raise Exception(f"Could not fetch data from {dataset_url}")


def clean(df:pd.DataFrame)->pd.DataFrame:
    """
    Fix dtype issue
    """
    try:
        df["lpep_pickup_datetime"] = pd.to_datetime(df["lpep_pickup_datetime"])
        df["lpep_dropoff_datetime"] = pd.to_datetime(df["lpep_dropoff_datetime"])
        logging.info(f"Data has {df.shape[0]} rows and {df.shape[1]} columns")
        return df
    except KeyError:
        logging.info("Dataframe does not have the expected columns")


def write_dataframe_to_s3_parquet(dataframe, bucket_name, s3_key):
    """
    Convert DataFrame to Parquet and save it in a bytes buffer
    """
    try:
        buffer = BytesIO()
        dataframe.to_parquet(buffer, compression='gzip')
        s3_resource = boto3.resource('s3')
        s3_resource.Object(bucket_name, s3_key).put(Body=buffer.getvalue())
        logging.info(f"Data saved to s3://{bucket_name}/{s3_key}")
    except Exception as e:
        logging.error(f"Could not save data to s3://{bucket_name}/{s3_key}")
        logging.error(str(e))
fetched_data = fetch_data(dataset_url)
cleaned_data = clean(fetched_data)
write_dataframe_to_s3_parquet(cleaned_data, "terraform-data-lake-666243375423", "test_s3_key")


