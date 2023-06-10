#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports

from flask import Flask, make_response, jsonify, request, session
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Column, Integer, String, ForeignKey, Float, Boolean, DateTime, Date, Text
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import datetime

# Local imports
from config import app, db, api
from models import User, Job, SavedJob, AppliedJob, Salary, CompanyReview, Company
from seed import fake

# Instantiate app, set attributes
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
# Define metadata, instantiate db
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)
db.init_app(app)

# Instantiate REST API
api = Api(app)
#-------bcrypt----------------

app = Flask(__name__)


# Views go here!


@app.route('/')
def index():
    return '<h1>WorkWander</h1>'



class User(Resource):
    def get(self):
        users = [user.tp_dict() for user in User.query.all()]
        return users
    
api.add_resource(User, '/users')


class Signup(Resource):
    def get(self, id):
        user = User.query.get(id)
        if user:
            return make_response(jsonify(user))
        else:
            return make_response(jsonify({'error': 'User not found'}), 404)

    def post(self):
        form_json = request.get_json()
        name = form_json('name')
        email = form_json('email')
        password = form_json('password')

        if not name or not email or not password:
            return jsonify({'error': 'Please include all fields'}), 400

        new_user = User(name=name, email=email)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id
        response = make_response(jsonify({'user': new_user.name}), 201)

        return response

api.add_resource(Signup, '/signup / <int:id>')

class Login(Resource):
    def post(self):
        form_json = request.get_json()
        email = form_json('email')
        password = form_json('password')

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
        saved_jobs = [saved_job.tp_dict() for saved_job in SavedJobs.query.all()]
        return saved_jobs
api.add_resource(SavedJobs, '/saved_jobs')

class AppliedJobs(Resource):
    def get(self):
        applied_jobs = [applied_job.tp_dict() for applied_job in AppliedJobs.query.all()]
        return applied_jobs
api.add_resource(AppliedJobs, '/applied_jobs')

class Salaries(Resource):
    def get(self):
        salaries = [salary.tp_dict() for salary in Salaries.query.all()]
        return salaries
api.add_resource(Salaries, '/salaries')


class CompanyReviews(Resource):
    def get(self):
        company_reviews = [company_review.tp_dict() for company_review in CompanyReviews.query.all()]
        return company_reviews
api.add_resource(CompanyReviews, '/company_reviews')


class Companies(Resource):
    def get(self):
        companies = [company.tp_dict() for company in Companies.query.all()]
        return companies
api.add_resource(Companies, '/companies')


if __name__ == '__main__':
    app.run(port=5555, debug=True)
