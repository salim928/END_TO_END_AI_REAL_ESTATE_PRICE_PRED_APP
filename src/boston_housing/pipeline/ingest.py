import os
import requests
import pandas as pd
from src.boston_housing.config import Configuration


def ingest_data():
    config = Configuration().data_ingestion_cfg
    os.makedirs(config.raw_data_dir, exist_ok=True)

    raw_path = config.raw_data_dir / config.raw_data_file
    # Download CSV
    resp = requests.get(config.data_source)
    resp.raise_for_status()
    with open(raw_path, "wb") as f:
        f.write(resp.content)

    # Quick sanity check
    df = pd.read_csv(raw_path)
    print(f"Ingested {len(df)} records to {raw_path}")


if __name__ == "__main__":
    ingest_data()