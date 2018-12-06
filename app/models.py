from app import db


class Traffic(db.Model):
    """database model for gov.uk traffic data."""

    __tablename__ = 'traffic'
    aadfyear = db.Column(db.Integer, primary_key=True)
    cp = db.Column(db.Integer, primary_key=True)
    estimationmethod = db.Column(db.String(30))
    estimationmethoddetailed = db.Column(db.String(200))
    region = db.Column(db.String(30))
    localauthority = db.Column(db.String(30))
    road = db.Column(db.String(10))
    roadcategory = db.Column(db.String(10))
    easting = db.Column(db.String(10))
    northing = db.Column(db.String(10))
    startjunction = db.Column(db.String(100))
    endjunction = db.Column(db.String(100))
    linklengthkm = db.Column(db.Float)
    linklengthmiles = db.Column(db.Float)
    pedalcycles = db.Column(db.Integer)
    motorcycles = db.Column(db.Integer)
    carstaxis = db.Column(db.Integer)
    busescoaches = db.Column(db.Integer)
    lightgoodsvehicles = db.Column(db.Integer)
    v2axlerigidhgv = db.Column(db.Integer)
    v3axlerigidhgv = db.Column(db.Integer)
    v4or5axlerigidhgv = db.Column(db.Integer)
    v3or4axleartichgv = db.Column(db.Integer)
    v5axleartichgv = db.Column(db.Integer)
    v6ormoreaxleartichgv = db.Column(db.Integer)
    allhgvs = db.Column(db.Integer)
    allmotorvehicles = db.Column(db.Integer)

    def __init__(self, aadfyear=None, cp=None):
        self.aadfyear = aadfyear
        self.cp = cp


