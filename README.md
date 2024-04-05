# Serhii Kushnir. Welcome to the repository with the application interview test task

This repository solves a task provided during the interview process 

## All reports and conclusions are stored in [Report Folder](docs/report)

## Pre-requirements
  - Python3.11
  - Python3-venv 
  - pip3

## Repository structure

**The repository contains some main folders and files:** 
- [app](app/) - folder with source code of application
- [deploy](deploy/) - folder with yaml file for deployment application to minikube
- [docs](docs/) - documentation folder
- [scripts](scripts/) - folder with a script to check application in minikube
- [Dockerfile](Dockerfile) - File for building a docker image 

## To run application locally: 
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 run.py
```

## To run the application in a production environment: 
There several steps are required to build and deploy the application for production needs.  
**Please refer to the [Documentation Build](docs/build/README.md) and [Documentation Deploy](docs/deploy/README.md)**
- **Run command:**
```
hypercorn --bind 0.0.0.0:5000 app:app
```