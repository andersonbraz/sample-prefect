
from prefect import flow, task

@task
def extrair_dados_api():
    print("Extraindo dados API...")

@flow(name="stage_raw_flow")
def stage_raw_flow():
    extrair_dados_api()
