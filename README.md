# learner-assessor-db-app

 ![image](https://github.com/user-attachments/assets/09e58a28-4574-4aa6-8957-ba6e5a8663df)
![image](https://github.com/user-attachments/assets/60554040-e4a4-43b4-9dbc-b8be885b9e6b)
![image](https://github.com/user-attachments/assets/bc6b0005-ba5b-4808-aad3-175fb1d5b4e0)
![image](https://github.com/user-attachments/assets/e8bdd763-93cb-4ef7-a9a0-f33832ad226e)
![image](https://github.com/user-attachments/assets/210a3969-c5be-44e2-8abd-2ede9996045c)
Project Overview
This project is a full-stack web application built using Flask for the backend and MySQL as the database. It manages three types of users: Learners, Assessors, and Institutions. The system allows registering these entities, storing their data in a relational database, and generating summary reports.

Database Design & Relationships
Institutions
Stores hospital or institution details such as name, address, state, pincode, and contact person info.

Learners
Stores learner details linked to an institution via a foreign key. Fields include full name, email, mobile, course, and batch.

Assessors
Stores assessor details linked to an institution. Includes full name, email, mobile, and role (Internal/External).

Relationships

Each Learner is linked to one Institution.

Each Assessor is linked to one Institution.

This structure ensures normalized data, avoiding duplicates and maintaining referential integrity.

How to Run and Test Locally
Prerequisites
Python 3.x installed

MySQL server installed and running

MySQL Workbench or any MySQL client (optional but recommended)

pip package manager

Setup Steps
Clone the repository



git clone <repo-url>
cd astrico_fse_app
Create MySQL database

Using MySQL Workbench or CLI, create the database:

sql

CREATE DATABASE astrico_fse_db;
Update config.py

Modify the SQLALCHEMY_DATABASE_URI in config.py with your MySQL credentials:



SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/astrico_fse_db'
Install dependencies


pip install -r requirements.txt
Initialize the database

If using Flask-Migrate (optional), else run:

from app import db
db.create_all()
Run the Flask app


python app.py
Access the application

Open your browser at http://localhost:5000. Use the navigation links or directly access forms for learners, assessors, and institutions.

Assumptions and Simplifications
Email and mobile number formats are assumed to be valid but are not strictly validated.

Institution names are unique to avoid duplicates.

Role for assessors is strictly "Internal" or "External".

No authentication implemented — it's an open system for demo purposes.

Frontend is simple HTML forms without advanced UI frameworks.

All forms submit data via POST and render simple success/error messages.

Data relationships are basic one-to-many (institution to learners/assessors).




