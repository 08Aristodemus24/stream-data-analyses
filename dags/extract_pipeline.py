import sys
import datetime as dt
import os
import shutil
import time

from pathlib import Path

from airflow import DAG, settings
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.papermill.operators.papermill import PapermillOperator
from airflow.models import Variable, Connection 
from airflow.configuration import conf

# go to this site if you want to use cron instead of datetime to set schedule_interval
# https://crontab.guru/#00_12_*_*_Sun




# get airflow folder
AIRFLOW_HOME = conf.get('core', 'dags_folder')

# base dir would be /opt/***/ or /opt/airflow
BASE_DIR = Path(AIRFLOW_HOME).resolve().parent

default_args = {
    'owner': 'mikhail',
    'retries': 3,
    'retry_delay': dt.timedelta(minutes=2)
}

with DAG(
    dag_id="extract_pipeline",
    default_args=default_args,
    description="extracts subreddit data from reddit api and queues the data in kafka",
    start_date=dt.datetime(2024, 1, 1, 12),

    # runs every sunday at 12:00 
    schedule="00 12 * * Sun",
    catchup=False
) as dag:
    
    fetch_reddit_data = BashOperator(
        task_id="extract_signals",
        bash_command=f"python {AIRFLOW_HOME}/operators/fetch_reddit_data.py"
    )