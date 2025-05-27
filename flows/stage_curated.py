
from prefect import flow, task

@task
def extrair_dados_raw():
    print("Extraindo dados RAW...")

@flow(name="stage_curated_flow")
def stage_curated_flow():
    extrair_dados_raw()
