#!/usr/bin/env python3

# Standard library imports
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'instance/app.db')}")

from flask import Flask, jsonify, make_response, request

from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

from models import db, User, Job, Company

# Instantiate Flask app
app = Flask(__name__)

# Configure app
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False


migrate = Migrate(app, db)

db.init_app(app)

# Instantiate REST API
api = Api(app)

# -------bcrypt----------------

# Import models after initializing db

# Views go here!


@app.route('/')
def index():
    return '<h1>WorkWander</h1>'


class UserList(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return make_response(jsonify(users), 200)
    
api.add_resource(UserList, '/users')
    
class UserListById(Resource):
    def get(self, id):
        user = User.query.get(id)
        if not user:
            return make_response({"error": "404: Camper not found."}, 404)
        return make_response(jsonify(user.to_dict()), 200)
    
api.add_resource(UserListById, '/users/<int:id>')



class JobList(Resource):
    def get(self):
        job_list = [job.to_dict() for job in Job.query.all()]
        return make_response(jsonify(job_list), 200)
    
    def delete(self):
        job_id = request.json.get('id')
        if job_id is None:
            return make_response(jsonify({'error': "400: Missing 'id' parameter"}), 400)

        job = Job.query.get(job_id)
        if job is None:
            return make_response(jsonify({'error': "404: Job not found"}), 404)

        db.session.delete(job)
        db.session.commit()
        return {}, 200


api.add_resource(JobList, '/jobs')



class CompanyList(Resource):
    def get(self):
        companies = [company.to_dict() for company in Company.query.all()]
        return make_response(jsonify(companies), 200)

api.add_resource(CompanyList, '/companies')


if __name__ == '__main__':
    app.run(port=5000, debug=True)