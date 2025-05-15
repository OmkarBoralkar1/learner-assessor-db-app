from .db import db

class Institution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    address = db.Column(db.Text)
    state = db.Column(db.String(100))
    pincode = db.Column(db.String(10))
    contact_name = db.Column(db.String(100))
    contact_email = db.Column(db.String(100))
    contact_mobile = db.Column(db.String(15))

    learners = db.relationship('Learner', backref='institution', lazy=True)
    assessors = db.relationship('Assessor', backref='institution', lazy=True)
