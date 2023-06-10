from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import validates
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask import request
from flask_restful import Resource
from config import db, app, api, jwt


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
db = SQLAlchemy(app)
jwt = JWTManager(app)

@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    if identity == 1:
        return {'is_admin': True}
    return {'is_admin': False}

@jwt.expired_token_loader
def expired_token_callback():
    return {
        'description': 'The token has expired.',
        'error': 'token_expired'
    }, 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return {
        'description': 'Signature verification failed.',
        'error': 'invalid_token'
    }, 401

@jwt.unauthorized_loader
def missing_token_callback(error):
    return {
        'description': 'Request does not contain an access token.',
        'error': 'authorization_required'
    }, 401

@jwt.needs_fresh_token_loader
def token_not_fresh_callback():
    return {
        'description': 'The token is not fresh.',
        'error': 'fresh_token_required'
    }, 401

@jwt.revoked_token_loader
def revoked_token_callback():
    return {
        'description': 'The token has been revoked.',
        'error': 'token_revoked'
    }, 401
    


# Models go here!

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    jobs = db.relationship('Jobs', backref='user')
    savedjobs = db.relationship('SavedJobs', backref='user')
    appliedjobs = db.relationship('AppliedJobs', backref='user')
    salaries = db.relationship('Salaries', backref='user')
    companyreviews = db.relationship('CompanyReviews', backref='user')
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def json(self):
        return {'username': self.username, 'password': self.password}
    
    def json_with_jobs(self):
        return {'username': self.username, 'password': self.password, 'jobs': self.jobs}
    
    def json_with_savedjobs(self):
        return {'username': self.username, 'password': self.password, 'savedjobs': self.savedjobs}
    
    def json_with_all(self):
        return {'username': self.username, 'password': self.password, 'jobs': self.jobs, 'savedjobs': self.savedjobs}

    @validates('username')
    def validate_username(self, key, username):
        if not username:
            raise AssertionError('No username provided')
        if User.query.filter(User.username == username).first():
            raise AssertionError('Username is already in use')
        if len(username) < 5 or len(username) > 20:
            raise AssertionError('Username must be between 5 and 20 characters')
        return username
    
    @validates('password')
    def validate_password(self, key, password):
        if not password:
            raise AssertionError('No password provided')
        if len(password) < 5 or len(password) > 20:
            raise AssertionError('Password must be between 5 and 20 characters')
        return password

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'username': x.username,
                'password': x.password
            }
        return {'users': list(map(lambda x: to_json(x), User.query.all()))}
    
    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
        except:
            return {'message': 'Something went wrong'}
    
    def __repr__(self):
        return f"<User {self.username}>"
    
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }
    
    def serialize_with_jobs(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'jobs': self.jobs
        }
    
    def serialize_with_savedjobs(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'savedjobs': self.savedjobs
        }
    
    def serialize_with_all(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'jobs': self.jobs,
            'savedjobs': self.savedjobs,
            'appliedjobs': self.appliedjobs,
            'salaries': self.salaries,
            'companyreviews': self.companyreviews
        }


class Job(db.Model, SerializerMixin):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    company = db.Column(db.String)
    location = db.Column(db.String)
    description = db.Column(db.String)
    salary = db.Column(db.Integer)
    link = db.Column(db.String)
    date = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='jobs')
    savedJobs = db.relationship('SavedJobs', backref='jobs')
    appliedJobs = db.relationship('AppliedJobs', backref='jobs')
    salaries = db.relationship('Salaries', backref='jobs')
    companyReviews = db.relationship('CompanyReviews', backref='jobs')

    def __init__(self, id, title, company, location, description, salary, link, date, user_id):
        self.id = id
        self.title = title
        self.company = company
        self.location = location
        self.description = description
        self.salary = salary
        self.link = link
        self.date = date
        self.user_id = user_id



    def __repr__(self):
        return f"<Job {self.title}>"
    
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'company': self.company,
            'location': self.location,
            'description': self.description,
            'salary': self.salary,
            'link': self.link,
            'date': self.date
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()
    
    @classmethod
    def find_by_company(cls, company):
        return cls.query.filter_by(company=company).first()
    
    @classmethod
    def find_by_location(cls, location):
        return cls.query.filter_by(location=location).first()
    
    @classmethod
    def find_by_description(cls, description):
        return cls.query.filter_by(description=description).first()
    
    @validates('salary')
    def validate_salary(self, key, salary):
        if salary is None:
            return None
        if salary[0] == '$':
            return salary
        else:
            return '$' + salary
        
    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'id': x.id,
                'title': x.title,
                'company': x.company,
                'location': x.location,
                'description': x.description,
                'salary': x.salary,
                'link': x.link,
                'date': x.date
            }
        return {'jobs': list(map(lambda x: to_json(x), Jobs.query.all()))}
    
    @validates('link')
    def validate_link(self, key, link):
        if link is None:
            return None
        if link[0:4] == 'http':
            return link
        else:
            return 'https://' + link
        
    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
        except:
            return {'message': 'Something went wrong'}
        
    def serialize_with_user(self):
        return {
            'id': self.id,
            'title': self.title,
            'company': self.company,
            'location': self.location,
            'description': self.description,
            'salary': self.salary,
            'link': self.link,
            'date': self.date,
            'user': self.user
        }
    
    def serialize_with_savedjobs(self):
        return {
            'id': self.id,
            'title': self.title,
            'company': self.company,
            'location': self.location,
            'description': self.description,
            'salary': self.salary,
            'link': self.link,
            'date': self.date,
            'savedjobs': self.savedjobs
        }
    
    def serialize_with_appliedjobs(self):
        return {
            'id': self.id,
            'title': self.title,
            'company': self.company,
            'location': self.location,
            'description': self.description,
            'salary': self.salary,
            'link': self.link,
            'date': self.date,
            'appliedjobs': self.appliedjobs
        }
    
    def serialize_with_salaries(self):
        return {
            'id': self.id,
            'title': self.title,
            'company': self.company,
            'location': self.location,
            'description': self.description,
            'salary': self.salary,
            'link': self.link,
            'date': self.date,
            'salaries': self.salaries
        }
    
    def serialize_with_companyreviews(self):
        return {
            'id': self.id,
            'title': self.title,
            'company': self.company,
            'location': self.location,
            'description': self.description,
            'salary': self.salary,
            'link': self.link,
            'date': self.date,
            'companyreviews': self.companyreviews
        }
    
    def serialize_with_all(self):
        return {
            'id': self.id,
            'title': self.title,
            'company': self.company,
            'location': self.location,
            'description': self.description,
            'salary': self.salary,
            'link': self.link,
            'date': self.date,
            'user': self.user,
            'savedjobs': self.savedjobs,
            'appliedjobs': self.appliedjobs,
            'salaries': self.salaries,
            'companyreviews': self.companyreviews
        }
    @validates('date')
    def validate_date(self, key, date):
        if date is None:
            return None
        if date[0:3] == 'Jun':
            return date
        else:
            return 'Jun ' + date
        
class SavedJob(db.Model, SerializerMixin):
    __tablename__ = 'saved_jobs'
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='savedjobs')

    def __init__(self, job_id, user_id):
        self.job_id = job_id
        self.user_id = user_id
    
    def __repr__(self):
        return f"<SavedJob {self.job_id}>"
    
    def serialize(self):
        return {
            'id': self.id,
            'job_id': self.job_id,
            'user_id': self.user_id
        }
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    @classmethod
    def find_by_job_id(cls, job_id):
        return cls.query.filter_by(job_id=job_id).first()

    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()
    
    @validates('job_id')
    def validate_job_id(self, key, job_id):
        if job_id is None:
            return None
        if job_id[0:3] == 'Jun':
            return job_id
        else:
            return 'Jun ' + job_id
        

class AppliedJob(db.Model, SerializerMixin):
    __tablename__ = 'applied_jobs'
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='appliedjobs')

    def __init__(self, job_id, user_id):
        self.job_id = job_id
        self.user_id = user_id

    def __repr__(self):
        return f"<AppliedJob {self.job_id}>"
    
    def serialize(self):
        return {
            'id': self.id,
            'job_id': self.job_id,
            'user_id': self.user_id
        }
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    @classmethod
    def find_by_job_id(cls, job_id):
        return cls.query.filter_by(job_id=job_id).first()
    
    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()
    
    @validates('job_id')
    def validate_job_id(self, key, job_id):
        if job_id is None:
            return None
        if job_id[0:3] == 'Jun':
            return job_id
        else:
            return 'Jun ' + job_id
        

class Salary(db.Model, SerializerMixin):
    __tablename__ = 'salaries'
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='salaries')
    salary = db.Column(db.Integer, nullable=False)

    def __init__(self, job_id, user_id, salary):
        self.job_id = job_id
        self.user_id = user_id
        self.salary = salary

    def __repr__(self):
        return f"<Salary {self.salary}>"
    
    def serialize(self):
        return {
            'id': self.id,
            'job_id': self.job_id,
            'user_id': self.user_id,
            'salary': self.salary
        }
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    @classmethod
    def find_by_job_id(cls, job_id):
        return cls.query.filter_by(job_id=job_id).first()
    
    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()
    
    @validates('job_id')
    def validate_job_id(self, key, job_id):
        if job_id is None:
            return None
        if job_id[0:3] == 'Jun':
            return job_id
        else:
            return 'Jun ' + job_id
        
    @validates('salary')
    def validate_salary(self, key, salary):
        if salary is None:
            return None
        if salary[0:3] == 'Jun':
            return salary
        else:
            return 'Jun ' + salary

class CompanyReview(db.Model, SerializerMixin):
    __tablename__ = 'company_reviews'
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='companyreviews')
    review = db.Column(db.String, nullable=False)
    rating = db.Column(db.String, nullable=False)
    company = db.Column(db.String, nullable=False)

    def __init__(self, job_id, user_id, review, rating, company):
        self.job_id = job_id
        self.user_id = user_id
        self.review = review
        self.rating = rating
        self.company = company

    def __repr__(self):
        return f"<CompanyReview {self.review}>"
    
    def serialize(self):
        return {
            'id': self.id,
            'job_id': self.job_id,
            'user_id': self.user_id,
            'review': self.review,
            'rating': self.rating,
            'company': self.company
        }
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    @classmethod
    def find_by_job_id(cls, job_id):
        return cls.query.filter_by(job_id=job_id).first()
    
    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()
    
    @validates('job_id')
    def validate_job_id(self, key, job_id):
        if job_id is None:
            return None
        if job_id[0:3] == 'Jun':
            return job_id
        else:
            return 'Jun ' + job_id
        
    @validates('rating')
    def validate_rating(self, key, rating):
        if rating is None:
            return None
        if rating[0:3] == 'Jun':
            return rating
        else:
            return 'Jun ' + rating  
        
    @validates('company')
    def validate_company(self, key, company):
        if company is None:
            return None
        if company[0:3] == 'Jun':
            return company
        else:
            return 'Jun ' + company
        
class Company(db.Model, SerializerMixin):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.String, nullable=False)
    reviews = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    job_id = db.Column(db.Integer, nullable=False)

    def __init__(self, company, title, location, description, salary, rating, reviews, url, date, job_id):
        self.company = company
        self.title = title
        self.location = location
        self.description = description
        self.salary = salary
        self.rating = rating
        self.reviews = reviews
        self.url = url
        self.date = date
        self.job_id = job_id

    def __repr__(self):
        return f"<Company {self.company}>"
    
    def serialize(self):
        return {
            'id': self.id,
            'company': self.company,
            'title': self.title,
            'location': self.location,
            'description': self.description,
            'salary': self.salary,
            'rating': self.rating,
            'reviews': self.reviews,
            'url': self.url,
            'date': self.date,
            'job_id': self.job_id
        }
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    @classmethod
    def find_by_job_id(cls, job_id):
        return cls.query.filter_by(job_id=job_id).first()
    
    @classmethod
    def find_by_company(cls, company):
        return cls.query.filter_by(company=company).first()
    
    @validates('job_id')
    def validate_job_id(self, key, job_id):
        if job_id is None:
            return None
        if job_id[0:3] == 'Jun':
            return job_id
        else:
            return 'Jun ' + job_id
        
    @validates('salary')
    def validate_salary(self, key, salary):
        if salary is None:
            return None
        if salary[0:3] == 'Jun':
            return salary
        else:
            return 'Jun ' + salary
        
    @validates('rating')
    def validate_rating(self, key, rating):
        if rating is None:
            return None
        if rating[0:3] == 'Jun':
            return rating
        else:
            return 'Jun ' + rating
        
    @validates('reviews')
    def validate_reviews(self, key, reviews):
        if reviews is None:
            return None
        if reviews[0:3] == 'Jun':
            return reviews
        else:
            return 'Jun ' + reviews
        
    @validates('date')
    def validate_date(self, key, date):
        if date is None:
            return None
        if date[0:3] == 'Jun':
            return date
        else:
            return 'Jun ' + date
