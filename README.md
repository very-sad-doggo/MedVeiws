# MedVeiws
Team work for hospital monitoring app.

This multiuser app will connect to one of the Moscow hospitals DB and displaying data for further analys. 
Projected for their own using and deploying on their own local server.


## Local Deployment


1. Open **Git Bash** (or **PowerShell**) to clone the repo
```bash
git clone https://github.com/vlf0/MedVeiws.git
```
2. Create ENV in root the same folder (in this example i use _virtualenv_ module):
```bash
virtualenv venv
```
3. Go to scripts folder (root_folder/venv/scripts/) and activate virtual environment by
typing activating command. For example - for windows powershell it will be 
```bash
.\activate.ps1
```

4. Go to _MedViews_ folder and type for change working branch:
```bash
   git checkout localdev_vlf
```
5. Go to project folder named _observer_ and type:
```bash
   pip install -r requirements.txt
```
6. After this step you can testing app:
```bash
   python manage.py runserver
```
## Install as systemd service (for Ubuntu)

1. Clone the repo
```bash
    git clone https://github.com/vlf0/MedVeiws.git
```

2. Make sure *install.sh* is executable. If not, make it one
```bash
chmod +x install.sh
```

3. Execute script
```bash
sudo ./install.sh
```

4. Wait for the output 

    **CURRENTLY THE SCRIPT DOES NOT RETURN EXECPTED OUTPUT AND LEAVES YOU LOGGED IN AS ROOT** 

    **THE REST OF THE OUTPUT IS SHOWN ONCE YOU EXIT ROOT'S SHELL**

    **WILL BE FIXED IN FURTHER COMMITS**

5. Start the service

```bash
sudo systemctl start observer.service
```

6. Once the service is up and running you can try to access the app connecting to **localhost:8081** via your browser

## ДОПИСАТЬ ТРЕТИЙ СЕРВИС ДЛЯ ЗАПОЛНЕНИЯ ПГ