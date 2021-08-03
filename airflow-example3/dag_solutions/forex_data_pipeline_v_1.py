# you need to instance the DAG object because is your datapipeline
from airflow import DAG

#import datetime 
from datetime import datetime, timedelta

# default args dictonary 
# specify the attributes of your tasks,  
default_args = {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "admin@localhost.com",
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}
#before retry wait 5 minutes

with DAG("forex_data_pipeline", start_date=datetime(2021, 1 ,1), 
    schedule_interval="@daily", default_args=default_args, catchup=False) as dag:
    None

# instance the object dag with the parameters ==> with DAG(parameters) as dag:

# forex_data_pipeline = id es unique across all the DAGS    
# start_date=datetime(2021, 1 ,1) = your data pipeline will start being scheduled on 01-January-2021 
# remember import datetime ==> from datetime import datetime, timedelta
# schedule_interval="@daily" ==> frecuency at which your DAG is gonign to be triggered , 
#   so means that every day your DAG is going to be tiggered every day at midnight 
# default_args=default_args = create a dictionary and define the commoun attributes of your taks (owner, retires , email etc)
#   to use timedelta you have to import it 
# catchup=False prevent for running all the non triggered DAGs beteween de current date and the start date 
