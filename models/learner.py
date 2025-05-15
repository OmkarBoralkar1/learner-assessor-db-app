from .db import db

class Learner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    mobile = db.Column(db.String(15))
    course = db.Column(db.String(100))
    batch = db.Column(db.String(100))
    institution_id = db.Column(db.Integer, db.ForeignKey('institution.id'))
