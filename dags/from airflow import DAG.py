from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'saeid',
    'start_date': datetime(2025, 5, 8),
}

with DAG(
    dag_id='provision_infra',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=['netops', 'infra'],
) as dag:

    run_script = BashOperator(
        task_id='run_provision_script',
        bash_command='echo "Provisioning infrastructure with Terraform..."',
    )
