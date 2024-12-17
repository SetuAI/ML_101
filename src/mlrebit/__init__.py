import os
import sys
import logging

# saves time stamp
# levelname : if running from root folder then root
# stores info for tracking

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# create log folder named logs
log_dir = "logs"

# we need to create a log file inside the directory called running_log.log
log_filepath = os.path.join(log_dir, "running_log_new.log")
# create using makedires, if it is not available it will create one 
os.makedirs(log_dir, exist_ok=True)

# set up logging to file
logging.basicConfig(
    level = logging.INFO, 
    format = logging_str, # we have defined logging_str 

    handlers=[
        logging.FileHandler(log_filepath), 
        logging.StreamHandler(sys.stdout)
    ]
)

# define logger object
logger = logging.getLogger("mlrebitLogger")

# you can execute this file in main.py
# you can import the logging
# from src.ML_REBIT_001.logging import logger