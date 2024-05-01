from . import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(500))
    answer = db.Column(db.String(10))