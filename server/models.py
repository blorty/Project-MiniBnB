from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Boolean, Table
from sqlalchemy.orm import relationship, backref, validates
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy
from flask import Flask, make_response, jsonify, request, session
from flask_restful import Api
from flask import request
from flask_restful import Resource
from config import db, app
import flask_bcrypt as bcrypt
from faker import Faker


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False


api = Api(app)
fake = Faker()


# Models go here!


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False, unique=True)
    _password_hash = Column(String, nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    created_at = Column(db.TIMESTAMP)

    jobs = db.relationship('Job', backref='users')

    @validates('username')
    def validate_username(self, key, username):
        if not username:
            raise AssertionError('No username provided')
        if User.query.filter(User.username == username).first():
            raise AssertionError('Username is already in use')
        if len(username) < 5 or len(username) > 20:
            raise AssertionError('Username must be between 5 and 20 characters')
        return username
    



    @property
    def password(self):
        raise AttributeError("Password issue")

    @password.setter
    def password(self, password):
        password_bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        self._password_hash = hashed_password.decode("utf-8")

    def authenticate(self, password):
        password_bytes = password.encode("utf-8")
        hashed_password = self._password_hash.encode("utf-8")
        return bcrypt.checkpw(password_bytes, hashed_password)


class Job(db.Model, SerializerMixin):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)

    title = Column(String, nullable=False)
    location = Column(String, nullable=False)
    salary = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    User_id = Column(Integer, ForeignKey('users.id'))
    company_id = Column(Integer, ForeignKey('companies.id'))
    company_review_id = Column(Integer, ForeignKey('company_reviews.id'))

    company = db.relationship('Company', backref='job')
    company_review = db.relationship('CompanyReview', backref='job')





class Company(db.Model, SerializerMixin):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    description = Column(String, nullable=False)
    industry = Column(String, nullable=False)
    website = Column(String, nullable=False)


    company_id = Column(Integer, ForeignKey('companies.id'))


class Salary(db.Model, SerializerMixin):
    __tablename__ = 'salaries'
    id = Column(Integer, primary_key=True)
    salary = Column(String, nullable=False)
    job_id = Column(Integer, ForeignKey('jobs.id'))
    User_id = Column(Integer, ForeignKey('users.id'))

    user = db.relationship('User', backref='salaries')
    job = db.relationship('Job', backref='salaries')



class CompanyReview(db.Model, SerializerMixin):
    __tablename__ = 'company_reviews'
    id = Column(Integer, primary_key=True)
    review = Column(String, nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id'))
    User_id = Column(Integer, ForeignKey('users.id'))

    company = db.relationship('Company', backref='company_reviews')


class AppliedJob(db.Model, SerializerMixin):
    __tablename__ = 'applied_jobs'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)
    applied_date = db.Column(db.Date, nullable=False)

    user = db.relationship('User', backref='applied_jobs')
    job = db.relationship('Job', backref='applied_jobs')



#TABLE RELATIONSHIPS (NEED TO WORK ON THIS....)
#SALARY -> JOB
#COMPANY REVIEW -> COMPANY
#APPLIED JOBS -> JOB, USER
#-----------------------------------------------------------------------------
