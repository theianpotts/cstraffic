import os
import postgres_copy
import tempfile, shutil, urllib

from app import app, db
from models import Traffic


def get_all_traffic():
    return Traffic.query.all()

def get_traffic_by_year(year):
    return Traffic.query.filter(Traffic.aadfyear == year).all()

def get_traffic_by_minusage(usage):
    return Traffic.query.filter(Traffic.allmotorvehicles >= usage).all()

def get_busiest_roads_by_year(year, count):
    return Traffic.query.filter(Traffic.aadfyear == year).order_by(Traffic.allmotorvehicles.desc()).with_entities(Traffic.road, Traffic.allmotorvehicles).limit(count).all()

def clear_data():
    numDeleted = Traffic.query.delete();
    db.session.commit()

    return numDeleted

def resync_data():
    try:
       clear_data()

       data = urllib.urlopen('http://api.dft.gov.uk/v3/trafficcounts/export/la/Devon.csv').read()

       fd, path = tempfile.mkstemp()
       os.write(fd, data)
       os.close(fd)

       with open(path) as fp:
           postgres_copy.copy_from(fp, Traffic, db.get_engine(), format='csv', header='true')

       os.remove(path)

       return Traffic.query.count()
    except Exception:
       return 0

