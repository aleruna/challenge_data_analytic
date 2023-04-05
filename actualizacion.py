#### subir a un repositorio un archivo de excel 
import git
import os


excel_path = "path/archivo.xlsx"


repositorio = "/path/to/repo"

# Configuración de la cuenta de Git
username = "usuario"
contraseña = "contraseña"

# Inicio
repo = git.Repo(repositorio)


repo.remotes.origin.pull()

#copia del archivo en la carpeta del repositorio
os.system(f"cp {excel_path} {repositorio}")

#añadir 
repo.index.add(["archivo.xlsx"])

#comentar cambios
repo.index.commit("Subo el archivo de excel")


repo.remotes.origin.push(username, contraseña)

################ DAG 

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 29),
    'retries': 1,
    'retry_delay': timedelta(hours=1),
}

dag = DAG(
    'actualizacion_datos',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
)

descargar_tarea = BashOperator(
    task_id='descarga',
    bash_command='python /path/to/descarga.py',
    dag=dag,
)

transformar_tarea = BashOperator(
    task_id='transformar',
    bash_command='python /path/to/transformar.py',
    dag=dag,
)

insertar_tarea = BashOperator(
    task_id='insertar',
    bash_command='python /path/to/insertar.py',
    dag=dag,
)


