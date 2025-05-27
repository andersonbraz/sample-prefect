from prefect import flow, task

@task
def extrair_dados_curated():
    print("Extraindo dados CURATED...")

@flow(name="stage_analytics_flow")
def stage_analytics_flow():
    extrair_dados_curated()
