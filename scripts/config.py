from pathlib import Path
import yaml

root = Path(__file__).resolve().parent.parent

with open(root/"config.yaml") as f:
    config = yaml.safe_load(f)

preprocessing = config["preprocessing"]
