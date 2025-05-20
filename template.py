import os
from pathlib import Path
import logging

# configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# your Python package under src/
project_pkg = 'boston_housing'

# list out all dirs/files to create
files_and_dirs = [
    # CI/CD
    ".github/workflows/.gitkeep",

    # configs
    "config/config.yaml",
    "config/params.yaml",

    # data & models
    "data/.gitkeep",
    "models/.gitkeep",

    # docs & notebooks
    "docs/.gitkeep",
    "notebooks/trials.ipynb",

    # pipeline definition
    "dvc.yaml",
    
    # project metadata
    "requirements.txt",
    "setup.py",

    # web templates
    "templates/.gitkeep",

    # source package
    f"src/{project_pkg}/__init__.py",
    f"src/{project_pkg}/components/__init__.py",
    f"src/{project_pkg}/config/__init__.py",
    f"src/{project_pkg}/constants/__init__.py",
    f"src/{project_pkg}/entity/__init__.py",
    f"src/{project_pkg}/pipeline/__init__.py",
    f"src/{project_pkg}/utils/__init__.py",

    # tests
    "tests/.gitkeep",
]

for path_str in files_and_dirs:
    path = Path(path_str)
    dirpath = path.parent

    # make directories
    if not dirpath.exists():
        os.makedirs(dirpath, exist_ok=True)
        logging.info(f"Created directory: {dirpath}")

    # touch files (only if they don’t already exist or are empty)
    if path.suffix == "" or not path.exists() or path.stat().st_size == 0:
        # for “.gitkeep” or empty placeholders, just touch
        path.touch(exist_ok=True)
        logging.info(f"Touched file: {path}")
    else:
        logging.info(f"Already exists: {path}")
