from .db import db

class Assessor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    mobile = db.Column(db.String(15))
    role = db.Column(db.Enum('Internal', 'External'))
    institution_id = db.Column(db.Integer, db.ForeignKey('institution.id'))
