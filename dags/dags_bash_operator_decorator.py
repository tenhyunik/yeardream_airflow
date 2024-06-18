from airflow.decorators import dag
import pendulum
from airflow.operators.bash import BashOperator

@dag(dag_id='dags_bash_operator_decorator',
     schedule="0 13 * * 5#2",
     start_date=pendulum.datetime(2024, 6, 1, tz="Asia/Seoul"),
     catchup=False,
     tags=['homework']
)
def dags_bash_operator_decorator():
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami"
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME"
    )

    bash_t1 >> bash_t2

dags_bash_operator_decorator()

#GPT Ver
# from airflow import DAG
# import pendulum
# from airflow.decorators import dag
# from airflow.operators.bash import BashOperator

# # @dag 데코레이터를 사용하여 DAG 정의
# @dag(
#     schedule_interval="0 13 * * 5#2",
#     start_date=pendulum.datetime(2024, 5, 1, tz="Asia/Seoul"),
#     catchup=False,
#     dag_id="dags_bash_operator",
#     tags=["homework"]
# )
# def create_dag():
#     # 작업 정의
#     bash_t1 = BashOperator(
#         task_id="bash_t1",
#         bash_command="echo whoami",
#     )

#     bash_t2 = BashOperator(
#         task_id="bash_t2",
#         bash_command="echo $HOSTNAME",
#     )

#     # 작업 종속성 설정
#     bash_t1 >> bash_t2

# # DAG 인스턴스화
# dag = create_dag()
