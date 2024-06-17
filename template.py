import os
import logging
from pathlib import Path

list_of_files = [
    ".github/workflow/.gitkeep",
     "experiment/search_engine.ipynb",
     "init_setup.sh",
     "requirements.txt",
     "app.py",
     "templates/index.html",
     ".gitignore"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Create directory: {filedir} for file:{filename}")
    if not os.path.exists(filepath)or(os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Create empty file: {filepath}")