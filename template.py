import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO ,
                    format='[%(asctime)s]:%(message)s:')

# https://docs.python.org/3/howto/logging.html

# create a project folder
project_name ="mlrebit"


# we need to define a list of files and folders 
# inside a list 
# create folder src , inside src create project name = ML REBIT 001

list_of_files = [
    f"src/{project_name}/__init__.py", # create one constructor file inside proj folder
    f"src/{project_name}/components/__init__.py", 
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

]

# create folders and files, loop through list of files
for filepath in list_of_files:
    filepath = Path(filepath)
    # Path class will detect the os as well
    # it will extract the Path and convert the / or \ as per the OS
    
    # once you get the path seperate the folder and file
    # For example, f"src/{project_name}/__init__.py
    # src/{project_name} tends to folder and __init__.py tends to file
    filedir, filename = os.path.split(filepath)
     
    # file directory creation using makedirs
    # if it already exists do not create, if it doesnt exist create it and log it
    # exist_ok  will check if exists or not 
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
        
    # Once the folder or directory has been created , now we create the file
    # first check if the file is available, if available, check file size if 0 or not
   
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f: # open file in write mode
            pass
            logging.info(f"Creating empty file: {filepath}") 

    # if the file is already available, do nothing
    else:
        logging.info(f"{filename} is already ex ists")

# run the code using python template.py and you can see changes being reflected 