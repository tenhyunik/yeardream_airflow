from airflow import DAG
import pendulum
from airflow.operators.bash import BashOperator

# 표준 생성자를 사용하여 DAG 정의
dag = DAG(
    dag_id="dags_bash_operator",
    schedule_interval="0 9 * * 1,5",
    start_date=pendulum.datetime(2024, 6, 1, tz="Asia/Seoul"),
    catchup=False,
    tags=["homework"]
)

# 작업 정의
bash_t1 = BashOperator(
    task_id="bash_t1",
    bash_command="echo whoami",
    dag=dag
)

bash_t2 = BashOperator(
    task_id="bash_t2",
    bash_command="echo $HOSTNAME",
    dag=dag
)

# 작업 종속성 설정
bash_t1 >> bash_t2
