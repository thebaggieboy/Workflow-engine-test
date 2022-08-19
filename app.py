from airflow import DAG
from datetime import datetime
from airflow.operators.python_operator import PythonOperator
from airflow.operators.base_operators import BaseOperator
from airflow.sensors.base.BaseSensorOperator

currentDateAndTime = datetime.now()

# Create a time range function
def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

# Define a send mail function 
def send_mail(to):
    print("Sending mail to recipients")


def welcome_message():
    print("Welcome there!, First DAG executed Successfully!!")

# Create a DAG operator base class
class MyWelcomeDAGOperator(BaseOperator):
    @apply_defaults
    def __init__(self, my_params, *args, **kwargs):
        self.task_my_params = my_params
        super(MyWelcomeDAGOperator).__init__(*args, **kwargs)

    def execute(self, context):
        log.info("Hello world!")
        log.info(f"my_params:{self.task_my_params}")

# Create a sensor that adds and checks for conditional nodes in the workflow engine
class TimeSensor(BaseSensorOperator):
    def poke(self, context):
        start = datetime.time(1, 0, 0)
        end = datetime.time(5, 0, 0)
        
        # Get the current time
        currentTime = currentDateAndTime.strftime("%H:%M:%S")
        t_range = time_in_range(start, end, currentTime)
        if t_range == True:
            log.info("The current time is", currentTime)
            send_mail("mofeodujirin@gmail.com")
            task_instance = context['task_instance']
            task_instance.xcom_push('sensors_time', currentTime)

            return True

        

# initialize the operator DAG       
operator_dag = DAG(dag_id="OperatorDAG", start_date=datetime(2022,8,18), schedule_interval="@hourly",
         catchup=False)


welcome_dag = DAG(dag_id="WelcomeDAG", start_date=datetime(2022,8,18), schedule_interval="@hourly",
         catchup=False)

with welcome_dag:
    welcome_task = PythonOperator(
    task_id="welcome_message_task",
    python_callable=welcome_message)

with operator_dag:
    my_operator_dag = PythonOperator(
        my_params='This is the first operator test',
        task_id='my_task'
    )

