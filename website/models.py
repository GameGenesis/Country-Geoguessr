from sqlalchemy.sql import func
from . import db

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String)
    answer = db.Column(db.String)