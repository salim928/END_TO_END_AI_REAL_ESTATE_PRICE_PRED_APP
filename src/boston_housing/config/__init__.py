from pathlib import Path
import yaml
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    data_source: str
    raw_data_dir: Path
    raw_data_file: str

@dataclass
class Configuration:
    config_path: Path = Path("config/config.yaml")
    params_path: Path = Path("params.yaml")

    def __post_init__(self):
        with open(self.config_path) as f:
            cfg = yaml.safe_load(f)
        self.data_ingestion_cfg = DataIngestionConfig(
            data_source=cfg["data_source"],
            raw_data_dir=Path(cfg["raw_data_dir"]),
            raw_data_file=cfg["raw_data_file"],
        )