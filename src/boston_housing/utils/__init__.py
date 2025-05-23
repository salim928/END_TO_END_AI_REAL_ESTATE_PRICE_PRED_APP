import os
import sys
import logging

# 1. Directory & filepath
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILEPATH = os.path.join(LOG_DIR, "running_logs.log")  # *.log is conventional

# 2. Formatter string — note %(message)s (singular), not %(messages)s
LOG_FORMAT = "[%(asctime)s - %(levelname)s - %(module)s]: %(message)s"

# 3. Configure root logger handlers
logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler(LOG_FILEPATH),
        logging.StreamHandler(sys.stdout),
    ],
)

# 4. Create & export your module-specific logger
logger = logging.getLogger("boston_housing")
