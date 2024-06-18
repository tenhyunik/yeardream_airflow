#GPT
from airflow import DAG
import pendulum
from airflow.operators.bash import BashOperator

# Define the DAG with specific parameters
with DAG(
    dag_id="dags_bash_select_fruit",
    schedule="10 0 * * 6#1",  # Every first Saturday of the month at 00:10
    start_date=pendulum.datetime(2024, 6, 14, tz="Asia/Seoul"),
    catchup=False
) as dag:

    # Task to grant permission to the shell script
    t0_grant_permission = BashOperator(
        task_id="t0_grant_permission",
        bash_command="chmod +x /opt/airflow/plugins/shell/select_fruit.sh",
    )

    # Task to select an orange
    t1_orange = BashOperator(
        task_id="t1_orange",
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh ORANGE",
    )

    # Task to select an avocado
    t2_avocado = BashOperator(
        task_id="t2_avocado",
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh AVOCADO",
    )

    # Set task dependencies
    t0_grant_permission >> t1_orange >> t2_avocado

#2nd Ver
# from airflow import DAG
# import pendulum
# from airflow.operators.bash import BashOperator

# with DAG(
#     dag_id="dags_bash_select_fruit",
#     schedule="10 0 * * 6#1",
#     start_date=pendulum.datetime(2024, 6, 14, tz="Asia/Seoul"),
#     catchup=False
# ) as dag:
#     t0_grant_permission = BashOperator(
#         task_id="t0_grant_permission",
#         bash_command="chmod +x /opt/airflow/plugins/shell/select_fruit.sh ",
#     )
#     t1_orange = BashOperator(
#         task_id="t1_orange",
#         bash_command="/opt/airflow/plugins/shell/select_fruit.sh ORANGE",
#     )

#     t2_avocado = BashOperator(
#         task_id="t2_avocado",
#         bash_command="/opt/airflow/plugins/shell/select_fruit.sh AVOCADO",
#     )

#     t0_grant_permission >> [t1_orange, t2_avocado]

# 1st Ver
# from airflow import DAG
# import pendulum
# from airflow.operators.bash import BashOperator

# with DAG(
#     dag_id="dags_bash_select_fruit",
#     schedule="10 0 * * 6#1",
#     start_date=pendulum.datetime(2024, 6, 14, tz="Asia/Seoul"),
#     catchup=False
# ) as dag:
    
#     t1_orange = BashOperator(
#         task_id="t1_orange",
#         bash_command="/opt/airflow/plugins/shell/select_fruit.sh ORANGE",
#     )

#     t2_avocado = BashOperator(
#         task_id="t2_avocado",
#         bash_command="/opt/airflow/plugins/shell/select_fruit.sh AVOCADO",
#     )

#     t1_orange >> t2_avocado