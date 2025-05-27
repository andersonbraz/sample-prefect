from prefect import flow
import time

from flows.stage_raw import stage_raw_flow
from flows.stage_curated import stage_curated_flow
from flows.stage_analytics import stage_analytics_flow

@flow(name="pipeline_principal")
def main_pipeline():
    print("Iniciando pipeline...")
    
    # Executa os flows na ordem desejada
    stage_raw_flow()
    time.sleep(2)
    stage_curated_flow()
    time.sleep(2)
    stage_analytics_flow()

    print("Pipeline finalizada com sucesso!")

if __name__ == "__main__":
    main_pipeline()
