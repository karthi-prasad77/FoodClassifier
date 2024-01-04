import os
from pathlib import Path
import logging

# logging info
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s;')

project_name = "FoodClassifier"

list_files = [
    ".github/workflows/.gitkeep",
    f"{project_name}/Classifier/data_setup.py",
    f"{project_name}/Classifier/engine.py",
    f"{project_name}/Classifier/model_builder.py",
    f"{project_name}/Classifier/train.py",
    f"{project_name}/Classifier/utils.py",
    f"models/",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "README.md",
    "research/experiment.ipynb",
    "Deployment/app.py",
    "Dockerfile"
]

for file in list_files:
    filepath = Path(file)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)):
        with open(filepath, "w") as files:
            pass
            logging.info(f"Creating Empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")