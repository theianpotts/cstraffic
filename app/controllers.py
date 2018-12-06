import json
import postgres_copy
import tempfile, shutil, urllib

from flask import Flask, render_template, request, Response
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from modelenc import AlchemyEncoder
from app import app
from models import Traffic

@app.route('/api/getalltraffic')
def get_all_traffic():
    traffico = Traffic.query.all()
    return json.dumps([t for t in traffico], cls=AlchemyEncoder)

@app.route('/api/gettrafficbyyear/<year>')
def get_traffic_by_year(year):
    traffico = Traffic.query.filter(Traffic.aadfyear == year).all()
    return json.dumps([t for t in traffico], cls=AlchemyEncoder)

@app.route('/api/gettrafficbyminusage/<usage>')
def get_traffic_by_minusage(usage):
    traffico = Traffic.query.filter(Traffic.allmotorvehicles >= usage).all()
    return json.dumps([t for t in traffico], cls=AlchemyEncoder)

@app.route('/api/cleardata')
def clear_data():
    numDeleted = Traffic.query.delete();
    db.session.commit()

    data = {
        'rows' : numDeleted
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    return resp

@app.route('/api/resyncdata')
def resync_data():
    numDeleted = Traffic.query.delete();
    db.session.commit()

    data = urllib.urlopen('http://api.dft.gov.uk/v3/trafficcounts/export/la/Devon.csv').read()

    fd, path = tempfile.mkstemp()
    os.write(fd, data)
    os.close(fd)

    with open(path) as fp:
        postgres_copy.copy_from(fp, Traffic, db.get_engine(), format='csv', header='true')

    os.remove(path)

    data = {
        'rows' : Traffic.query.count()
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    return resp

