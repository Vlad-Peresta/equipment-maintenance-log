# Equipment Maintenance Log

An equipment maintenance log is a register that organizations use 
to record asset maintenance activities

## Check it out!

[Equipment Maintenance Log deployed to Render](https://equipment-maintenance-log.onrender.com/)

## Installation

Python3 must be already installed

#### Download the code
```angular2html
git clone git@github.com:Vlad-Peresta/equipment_maintenance_log.git
cd py-taxi-service-deploying
```

#### Set Up for Unix, macOS
```angular2html
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Set Up for Windows
```angular2html
python3 -m venv venv
.\env\Scripts\activate
pip3 install -r requirements.txt
```

#### Set Up Database
```angular2html
python3 manage.py makemigrations
python3 manage.py migrate
```

#### Start the app
```angular2html
python manage.py runserver
```

## Features

* Authentication functionality for Worker/User
* Managing workers, tasks and logs directly from website
* Admin panel for advanced management

## Testing website

You can use following superuser for testing website:
* Login: admin.user
* Password: 1qazcde3

## Project screenshots