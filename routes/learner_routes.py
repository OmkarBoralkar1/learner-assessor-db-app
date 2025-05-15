from flask import Blueprint, render_template, request, redirect, flash
from models.learner import Learner
from models.institution import Institution
from models.db import db

learner_bp = Blueprint('learner', __name__)

@learner_bp.route('/learners/add', methods=['GET', 'POST'])
def add_learner():
    if request.method == 'POST':
        data = request.form

        # Print all form data as ImmutableMultiDict
        print("Received form data:", data)

        # If you want to print individual fields:
        print("Full Name:", data.get('full_name'))
        print("Email:", data.get('email'))
        print("Mobile:", data.get('mobile'))
        print("Institution Name:", data.get('institution_name'))
        print("Course:", data.get('course'))
        print("Batch:", data.get('batch'))

        institution = Institution.query.filter_by(name=data['institution_name']).first()
        if institution:
            learner = Learner(
                full_name=data['full_name'],
                email=data['email'],
                mobile=data['mobile'],
                course=data.get('course'),
                batch=data.get('batch'),
                institution_id=institution.id
            )
            db.session.add(learner)
            db.session.commit()
            flash('Learner added successfully!', 'success')
            return redirect('/')
    return render_template('learner_form.html')
