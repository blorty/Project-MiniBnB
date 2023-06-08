#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_bcrypt import Bcrypt
from flask_mail import Mail, Message

# Local imports
from config import app, db, api
from models import User, Job, SavedJobs, AppliedJobs, Salaries, CompanyReviews, Companies
from seed import fake


# Views go here!

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>WorkWander</h1>'

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    serialized_users = [
        {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }
        for user in users
    ]
    return jsonify(serialized_users)

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if user:
        serialized_user = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }
        return jsonify(serialized_user)
    else:
        return jsonify({'error': 'User not found'}), 404
    
@app.route('/jobs', methods=['GET'])



