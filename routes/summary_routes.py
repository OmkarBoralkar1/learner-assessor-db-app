from flask import Blueprint, render_template, jsonify
from models.learner import Learner
from models.assessor import Assessor
from models.institution import Institution

summary_bp = Blueprint('summary', __name__)

@summary_bp.route('/summary/', methods=['GET'])
def summary():
    learners = Learner.query.count()
    assessors = Assessor.query.count()
    institutions = Institution.query.count()
    return render_template('summary.html', learners=learners, assessors=assessors, institutions=institutions)
