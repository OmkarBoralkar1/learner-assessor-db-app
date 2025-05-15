from flask import Blueprint, render_template, request, redirect
from models.assessor import Assessor
from models.institution import Institution
from models.db import db

assessor_bp = Blueprint('assessor', __name__)

@assessor_bp.route('/assessors/add', methods=['GET', 'POST'])
def add_assessor():
    if request.method == 'POST':
        data = request.form
        institution = Institution.query.filter_by(name=data['institution_name']).first()
        if institution:
            assessor = Assessor(
                full_name=data['full_name'],
                email=data['email'],
                mobile=data['mobile'],
                role=data['role'],
                institution_id=institution.id
            )
            db.session.add(assessor)
            db.session.commit()
               # ✅ Print success message
            print("✅ assessor added successfully to the database!")

            return redirect('/')
        else:
            print("⚠️ assessor was not able to add successfully .")
    return render_template('assessor_form.html')
