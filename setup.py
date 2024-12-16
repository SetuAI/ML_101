import setuptools

# read the README.md file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# project version mention : intial implementation , hence 0.0.0
__version__ = "0.0.0"
 
REPO_NAME = "ML_101" 
AUTHOR_USER_NAME = "SetuAI"
SRC_REPO = "ML_REBIT_001" # source repository inside src folder
AUTHOR_EMAIL = "chirantandatascience@gmail.com"

# now with setuptools.setup we will setup the src folder as local package
# which means if you want to do inter file imports , you can do it
# for example  code in config.py can be referenced from init.py

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
