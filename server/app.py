#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports

from flask import Flask, make_response, jsonify, request, session
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


migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)

#-------bcrypt----------------

app = Flask(__name__)
bcrypt = Bcrypt(app)


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

if __name__ == '__main__':
    app.run(port=5555, debug=True)