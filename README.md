---
services: app-service\web,app-service
platforms: python
author: theianpotts
---

This is a Python application making use of Flask and PostgreSQL to provide api calls to view and query data about road traffic on South West England roads.

It is hosted on Azure and may be viewed at:

 http://csiptrafficapi.azurewebsites.net/

This home page provides a list and description of the various API calls available.

The code can be downloaded and built locally, but will make use of the DB as hosted in Azure. The environment variable 'DBPASS' will need to be set with the password for access to the DB (available from the author).

Once the code is downloaded... run the following in PowerShell on Windows.

(CD to folder where code is downloaded)

pip install virtualenv
virtualenv venv
venv/Scripts/activate
pip install -r requirements.txt
cd app
Set-Item Env:FLASK_APP ".\app.py"
Set-Item DBPASS "xxxxxx" 
flask db upgrade
flask run

Then browse to:
http://127.0.0.1:5000/

