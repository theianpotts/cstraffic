import os
import json
import postgres_copy
import tempfile, shutil, urllib

from flask import Flask, render_template, request, Response
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from modelenc import AlchemyEncoder

database_uri = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
	dbuser='manager@ip-postgres-tests',
	dbpass='supersecretpass',
	dbhost='ip-postgres-tests.postgres.database.azure.com',
	dbname='cstasktraffic'

	)
  #  dbuser=os.environ['DBUSER'],
  #  dbpass=os.environ['DBPASS'],
  #  dbhost=os.environ['DBHOST'],
  #  dbname=os.environ['DBNAME']
#)

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# initialize the database connection
db = SQLAlchemy(app)

# initialize database migration management
migrate = Migrate(app, db)

from models import Traffic
from controllers import get_all_traffic, get_traffic_by_year, get_traffic_by_minusage, clear_data, resync_data

# The following provides a few UI pages to view and edit data to assist testing

@app.route('/')
def api_details():
    return render_template('apis.html')

@app.route('/list')
def view_traffic():
    traffic = Traffic.query.all()
    return render_template('traffic_list.html', traffic=traffic)

@app.route('/add', methods=['GET'])
def view_add_form():
    return render_template('add_traffic.html')

@app.route('/add', methods=['POST'])
def add_traffic():
    aadfyear = request.form.get('aadfyear')
    cp = request.form.get('cp')

    traffic = Traffic(aadfyear, cp)
    db.session.add(traffic)
    db.session.commit()

    return render_template(
        'add_done.html', aadfyear=aadfyear, cp=cp)



