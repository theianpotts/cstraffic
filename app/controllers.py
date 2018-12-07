import json

from flask import Response
from modelenc import AlchemyEncoder
from app import app
from services import get_all_traffic, get_traffic_by_year, get_traffic_by_minusage, get_busiest_roads_by_year, clear_data, resync_data

@app.route('/api/getalltraffic')
def api_get_all_traffic():
    traffic = get_all_traffic()
    return json.dumps([t for t in traffic], cls=AlchemyEncoder)

@app.route('/api/gettrafficbyyear/<year>')
def api_get_traffic_by_year(year):
    traffic = get_traffic_by_year(year)
    return json.dumps([t for t in traffic], cls=AlchemyEncoder)

@app.route('/api/gettrafficbyminusage/<usage>')
def api_get_traffic_by_minusage(usage):
    traffic = get_traffic_by_minusage(usage)
    return json.dumps([t for t in traffic], cls=AlchemyEncoder)

@app.route('/api/getbusiestroadsbyyear/<year>/<count>')
def api_get_busiest_roads_by_year(year, count):
    traffic = get_busiest_roads_by_year(year, count)
    return json.dumps([t for t in traffic], cls=AlchemyEncoder)

@app.route('/api/cleardata')
def api_clear_data():
    numDeleted = clear_data()

    data = {
        'rows' : numDeleted
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    return resp

@app.route('/api/resyncdata')
def api_resync_data():
    count = resync_data()

    data = {
        'rows' : count
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    if count == 0:
        resp.status = 500;
    return resp

