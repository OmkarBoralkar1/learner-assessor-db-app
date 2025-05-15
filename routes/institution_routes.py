from flask import Blueprint, render_template, request, redirect
from models.institution import Institution
from models.db import db

institution_bp = Blueprint('institution', __name__)

@institution_bp.route('/institutions/add', methods=['GET', 'POST'])
def add_institution():
    if request.method == 'POST':
        data = request.form

        # Print received form data
        print("Received form data:", data)
        print("Institution Name:", data.get('name'))
        print("Address:", data.get('address'))
        print("State:", data.get('state'))
        print("Pincode:", data.get('pincode'))
        print("Contact Name:", data.get('contact_name'))
        print("Contact Email:", data.get('contact_email'))
        print("Contact Mobile:", data.get('contact_mobile'))

        existing = Institution.query.filter_by(name=data['name']).first()
        if not existing:
            institution = Institution(
                name=data['name'],
                address=data['address'],
                state=data['state'],
                pincode=data['pincode'],
                contact_name=data['contact_name'],
                contact_email=data['contact_email'],
                contact_mobile=data['contact_mobile']
            )
            db.session.add(institution)
            db.session.commit()

            # ✅ Print success message
            print("✅ Institution added successfully to the database!")

            return redirect('/')
        else:
            print("⚠️ Institution already exists. Skipping insert.")
   
    return render_template('institution_form.html')
