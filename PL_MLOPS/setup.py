import io
import os
from pathlib import Path

from setuptools import find_packages,setup

NAME = "Prediction_Model"
DESCRIPTION = "Loan_Prediction_Model"
URL= "https://github.com/sohomgit"
EMAIL_ID = "sohom.ban96@gmail.com"
AUTHOR = "SOHOM BANERJEE"
REQUIRES_PYTHON =">=3.7.0"

# To get the parent folder name
pwd = os.path.abspath(os.path.dirname(__file__))
print(pwd)


# Get the list of requirements to be installed
def list_reqs(fname="requirements.txt"):
    with io.open(os.path.join(pwd,fname),encoding='utf-8') as f:
        return f.read().splitlines()

try:
    with io.open(os.path.join(pwd,"README.md"),encoding='utf-8') as f:
        long_description = "\n" + f.read()
except FileNotFoundError as e:
    long_description = DESCRIPTION


ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR/NAME
about ={}
with open(PACKAGE_DIR/'VERSION') as f:
    _version = f.read().strip()
    about["__version__"] = _version

setup(
    name= NAME,
    version=about["__version__"],
    long_description=long_description,
    long_description_content_type = "text/markdown",
    author= AUTHOR,
    author_email= EMAIL_ID,
    python_requires = REQUIRES_PYTHON,
    url= URL,
    packages= find_packages(exclude=("tests",)),
    package_data= {'prediction_model':['VERSION']},
    install_requires = list_reqs(),
    extras_require ={},
    include_package_data= True,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
         "Programming Language :: Python :: Implementation :: PyPy"


    ]
)