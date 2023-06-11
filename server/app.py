#!/usr/bin/env python3

# Standard library imports
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource
from flask import request, jsonify, make_response, session

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
from models import User, Job, AppliedJob, Salary, CompanyReview, Company

# Views go here!


@app.route('/')
def index():
    return '<h1>WorkWander</h1>'


class Users(Resource):
    def get(self):
        users = [user.tp_dict() for user in User.query.all()]
        return users


api.add_resource(Users, '/users')


class Jobs(Resource):
    def get(self):
        jobs = [job.tp_dict() for job in Job.query.all()]
        return jobs
    
    def delete(self):
        job = Job.query.get(request.json['id'])
        db.session.delete(job)
        db.session.commit()
        return job.to_dict()


api.add_resource(Jobs, '/jobs')


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
    
    def post(self):
        company_review = CompanyReview(
            user_id=request.json['user_id'],
            company_id=request.json['company_id'],
            review=request.json['review'],
            rating=request.json['rating']
        )


api.add_resource(CompanyReviews, '/company-reviews')


class Companies(Resource):
    def get(self):
        companies = [company.tp_dict() for company in Company.query.all()]
        return companies


api.add_resource(Companies, '/companies')


if __name__ == '__main__':
    app.run(debug=True)

