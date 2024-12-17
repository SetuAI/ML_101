#### ML_101
repo contains ML related stuff - docs, codes, datasets, books, PPTs

if using bash terminal  you can create files using touch command
for example, touch template.py and push it on github 


#### create virtual env 
in our base env we have many packages installed so we are using venv

"""
bash :

conda create -n mlrebit python=3.10 -y

#### JFK : -p
conda create -p mlrebit python=3.10 -y
#### when you use -p the env is created within the project structure locally

to activate the venv
conda activate mlrebit

requirement installation command
pip install -r requirements.txt

"""

#### Blog for YAML
https://medium.com/analytics-vidhya/how-to-write-configuration-files-in-your-machine-learning-project-47bc840acc19


#### writing project utility 
logging,exceptions and utils module

why we need logging ? 
Inside src, we have ML rebit folder (this is user defined)
Inside the same, we have __init__.py (constructor file)
we will use constructor file for logging purposes
OR you can also create another folder for logging purposes.

