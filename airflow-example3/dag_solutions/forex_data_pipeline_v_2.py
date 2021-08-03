from airflow import DAG
from airflow.providers.http.sensors.http import HttpSensor

from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "admin@localhost.com",
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

#### STEP 2
####22. Check is the API is available 
# THe goal is to add the task in order to check if the URL, is available
# TO ADD AN OPERATOR YOU NEED TO IMPORT IT 
# from airflow.providers.http.sensors.http import HttpSensor
# make a variable is_forex_rates_available to use the operator 

with DAG("forex_data_pipeline", start_date=datetime(2021, 1 ,1), 
    schedule_interval="@daily", default_args=default_args, catchup=False) as dag:

    is_forex_rates_available = HttpSensor(
        task_id="is_forex_rates_available",
        http_conn_id="forex_api",
        endpoint="marclamberti/f45f872dea4dfd3eaa015a4a1af4b39b",  #anything that youu have after de host
        response_check=lambda response: "rates" in response.text, #lambda funcion
        poke_interval=5,  # frecuency at which your sensor is going to check , every 5 seconds will check if the url is available
        timeout=20 # despues de 20 segundos/ if you do not specify the time out the sensor will run foreva
    )    

###END STEP2