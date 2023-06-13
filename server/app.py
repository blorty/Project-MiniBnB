#!/usr/bin/env python3

# Standard library imports
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'instance/app.db')}")


from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, make_response, session
from datetime import datetime
from os import environ
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
import secrets


from models import db, User, Job, Company


load_dotenv('.env')




bcrypt = Bcrypt()  # Fix variable name

# Instantiate Flask app
app = Flask(__name__)

#Set secret key
app.secret_key = environ.get('SECRET_KEY')

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
        jobs = [job.to_dict() for job in Job.query.all()]
        return make_response(jsonify(jobs), 200)

api.add_resource(JobList, '/jobs')
    

class JobListById(Resource):
    def get(self, id):
        job = Job.query.get(id)
        if job:
            return make_response(jsonify(job.to_dict()))
        return {'error': '404: Job not found'}, 404


    def delete(self, id):
        job = Job.query.get(id)
        if not job:
            return {'error': '404: Job not found'}, 404

        db.session.delete(job)
        db.session.commit()

        return make_response(jsonify({'message': 'Job deleted successfully'}), 200)


api.add_resource(JobListById, '/jobs/<int:id>')


class CompanyList(Resource):
    def get(self):
        companies = [company.to_dict() for company in Company.query.all()]
        return make_response(jsonify(companies), 200)

api.add_resource(CompanyList, '/companies')

class CompanyListById(Resource):
    def get(self, id):
        company = Company.query.get(id)
        if company:
            return make_response(jsonify(company.to_dict()))
        return {'error': '404: Company not found'}, 404

    def delete(self, id):
        company = Company.query.get(id)
        if not company:
            return {'error': '404: Company not found'}, 404

        db.session.delete(company)
        db.session.commit()

        return make_response(jsonify({'message': 'Company deleted successfully'}), 200)
    
api.add_resource(CompanyListById, '/companies/<int:id>')



class Signup(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return make_response(jsonify({'error': 'Invalid request data'}), 400)

        password = data.get('password')
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        user = User(username=data.get('username'), password=hashed_password, email=data.get('email'))
        user.created_at = datetime.now()

        db.session.add(user)
        db.session.commit()

        session['user_id'] = user.id

        return make_response(jsonify({'message': 'User created successfully'}), 201)

api.add_resource(Signup, '/signup')


@app.route('/create_job', methods=['POST'])
def create_job():
    data = request.get_json()
    if not data or 'title' not in data or 'description' not in data or 'location' not in data or 'salary' not in data:
        return make_response(jsonify({'error': 'Invalid request data'}), 400)

    job_title = data['title']
    job_location = data['location']
    job_salary = data['salary']
    job_description = data['description']

    job = Job(title=job_title, location=job_location, salary=job_salary, description=job_description)
    db.session.add(job)
    db.session.commit()

    return make_response(jsonify({'message': 'Job added successfully'}), 201)


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return make_response(jsonify({'error': 'Invalid request data'}), 400)

    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if not user or not bcrypt.check_password_hash(user.password, password):
        return make_response(jsonify({'error': 'Invalid username or password'}), 401)

    session['user_id'] = user.id

    return make_response(jsonify({'message': 'Logged in successfully', 'user_id': user.id}), 200)


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)  # Remove user ID from the session
    return make_response(jsonify({'message': 'Logged out successfully'}), 200)



if __name__ == '__main__':
    app.run(port=5000, debug=True)