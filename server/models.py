
from flask import Flask
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, TIMESTAMP
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
import flask_bcrypt as bcrypt
from faker import Faker
from flask_bcrypt import bcrypt

convention = {
  "ix": "ix_%(column_0_label)s",
  "uq": "uq_%(table_name)s_%(column_0_name)s",
  "ck": "ck_%(table_name)s_%(constraint_name)s",
  "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
  "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)
fake = Faker()


# Models go here!
# Models go here!


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False, unique=True)
    _password_hash = Column(String, nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    created_at = Column(db.TIMESTAMP)

    jobs = db.relationship('Job', backref='user')
    companies = association_proxy('jobs', 'company')
    
    
    @validates('username')
    def validate_username(self, key, username):
        if not username:
            raise AssertionError('No username provided')
        if User.query.filter(User.username == username, User.id != self.id).first():
            raise AssertionError('Username is already in use')
        if len(username) < 3 or len(username) > 20:
            raise AssertionError('Username must be between 3 and 20 characters')
        return username
    
    def __repr__(self):
        return f"<User {self.username}>"

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
    


    
class Company(db.Model, SerializerMixin):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)
    industry = Column(String, nullable=False)
    website = Column(String, nullable=False)

    jobs = db.relationship('Job', backref='company')
    users = association_proxy('jobs', 'user')
    


class Job(db.Model, SerializerMixin):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    location = Column(String, nullable=False)
    salary = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    company_id = Column(Integer, ForeignKey('companies.id'))

    serialize_rules = ('-user', '-company', )