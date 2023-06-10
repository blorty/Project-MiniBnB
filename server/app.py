#!/usr/bin/env python3

# Standard library imports
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource

# Instantiate Flask app
app = Flask(__name__)

# Configure app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workwander.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Instantiate db
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Instantiate REST API
api = Api(app)

# -------bcrypt----------------

# Import models after initializing db
from models import User, Job, SavedJob, AppliedJob, Salary, CompanyReview, Company

# Views go here!


@app.route('/')
def index():
    return '<h1>WorkWander</h1>'


class UserResource(Resource):
    def get(self):
        users = [user.tp_dict() for user in User.query.all()]
        return users


api.add_resource(UserResource, '/users')


class Signup(Resource):
    def get(self, id):
        user = User.query.get(id)
        if user:
            return make_response(jsonify(user))
        else:
            return make_response(jsonify({'error': 'User not found'}), 404)

    def post(self):
        form_json = request.get_json()
        name = form_json.get('name')
        email = form_json.get('email')
        password = form_json.get('password')

        if not name or not email or not password:
            return jsonify({'error': 'Please include all fields'}), 400

        new_user = User(name=name, email=email)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id
        response = make_response(jsonify({'user': new_user.name}), 201)

        return response


api.add_resource(Signup, '/signup/<int:id>')


class Login(Resource):
    def post(self):
        form_json = request.get_json()
        email = form_json.get('email')
        password = form_json.get('password')

        if not email or not password:
            return jsonify({'error': 'Please include all fields'}), 400

        user = User.query.filter_by(email=email).first()

        if not user or not user.check_password(password):
            return jsonify({'error': 'Invalid credentials'}), 401

        session['user_id'] = user.id
        response = make_response(jsonify({'user': user.name}), 200)

        return response


api.add_resource(Login, '/login')


class Logout(Resource):
    def post(self):
        session.clear()
        return make_response(jsonify({'message': 'Logged out'}), 200)


api.add_resource(Logout, '/logout')


class Jobs(Resource):
    def get(self):
        jobs = [job.tp_dict() for job in Job.query.all()]
        return jobs


api.add_resource(Jobs, '/jobs')


class SavedJobs(Resource):
    def get(self):
        saved_jobs = [saved_job.tp_dict() for saved_job in SavedJob.query.all()]
        return saved_jobs


api.add_resource(SavedJobs, '/saved-jobs')


class AppliedJobs(Resource):
    def get(self):
        applied_jobs = [applied_job.tp_dict() for applied_job in AppliedJob.query.all()]
        return applied_jobs


api.add_resource(AppliedJobs, '/applied-jobs')


class Salaries(Resource):
    def get(self):
        salaries = [salary.tp_dict() for salary in Salary.query.all()]
        return salaries


api.add_resource(Salaries, '/salaries')


class CompanyReviews(Resource):
    def get(self):
        company_reviews = [company_review.tp_dict() for company_review in CompanyReview.query.all()]
        return company_reviews


api.add_resource(CompanyReviews, '/company-reviews')


class Companies(Resource):
    def get(self):
        companies = [company.tp_dict() for company in Company.query.all()]
        return companies


api.add_resource(Companies, '/companies')


if __name__ == '__main__':
    app.run(debug=True)

