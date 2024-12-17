from src.mlrebit.logging import logger
# inside src folder, we have mlrebir folder
# inside mlrebit folder we have logging folder
# then we import logger which is defined while creating loggers

# you can execute this to check if logging works

logger.info("this is my custom log")
# you can see the output
# [2024-12-17 10:08:22,209: INFO: main: this is my custom log]
# this shows the message and the current timestamp and runnning from main.py
# similarly in the left pane you can see it has created a folder called logs
# under logs you can spot the log directory you defined while wriiting logger file

