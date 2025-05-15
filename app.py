from flask import Flask, render_template
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from models.db import db
from routes.learner_routes import learner_bp
from routes.assessor_routes import assessor_bp
from routes.institution_routes import institution_bp
from routes.summary_routes import summary_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)

# Register Blueprints
app.register_blueprint(learner_bp)
app.register_blueprint(assessor_bp)
app.register_blueprint(institution_bp)
app.register_blueprint(summary_bp)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5013)


