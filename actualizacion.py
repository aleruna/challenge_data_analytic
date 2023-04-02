#### subir a un repositorio un archivo de excel 
import git
import os

# Ruta local del archivo Excel
excel_path = "path/archivo.xlsx"

# Ruta del repositorio de Git
repositorio = "/path/to/repo"

# Configuración de la cuenta de Git
username = "usuario"
contraseña = "contraseña"

# Iniciar repositorio de git
repo = git.Repo(repositorio)

# actualizar repo
repo.remotes.origin.pull()

# copia del archivo en la carpeta del repositorio
os.system(f"cp {excel_path} {repositorio}")

# Añadir el archivo
repo.index.add(["archivo.xlsx"])

# Confirmar los cambios
repo.index.commit("Subo el archivo de excel")

# Empujar los cambios al repositorio remoto
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
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'actualizacion_datos',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
)

descargar_tarea = BashOperator(
    task_id='descargar_datos',
    bash_command='python /path/to/descargar_datos.py',
    dag=dag,
)

transformar_tarea = BashOperator(
    task_id='transformar_datos',
    bash_command='python /path/to/transformar_datos.py',
    dag=dag,
)

insertar_tarea = BashOperator(
    task_id='insertar_datos',
    bash_command='python /path/to/insertar_datos.py',
    dag=dag,
)

descargar_tarea >> transformar_tarea >> insertar_tarea