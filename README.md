# MedVeiws
Team work for hospital monitoring app.

This multiuser app will connect to one of the Moscow hospitals DB and displaying data for further analys. 
Projected for their own using and deploying on their own local server.

To deploy the application locally follow these steps:


1. Open **Git Bash** (or **PowerShell**) console and 
go to folder where you want to place the app;
2. Copy and past this code snippet to download repo:
```bash
    git clone https://github.com/vlf0/MedVeiws.git
```
3. Create **ENV** in project's root directory :
```bash
    cd MedVeiws
    virtualenv venv
```
4. Go to scripts folder (root_folder/venv/scripts/) and activate virtual environment by
typing activating command. For example - for windows powershell it will be 
```powershell
    .\activate.ps1
```
5. Go to _MedViews_ folder and type for change working branch:
```bash
   git checkout localdev_vlf
```
6. Go to project folder named _observer_ and type:
```bash
   pip install -r requirements.txt
```
7. After this step you can testing app:
```bash
   python manage.py runserver
```


# Запуск через 