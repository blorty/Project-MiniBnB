#!/usr/bin/env python3
from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, User, Job, SavedJobs, AppliedJobs, Salaries, CompanyReviews, Companies
from seed import fake
from config import app
from random import randint, choice as rc


with app.app_context():
    db.init_app(app)
    db.create_all()

    print("Deleting data...")
    User.query.delete()
    Job.query.delete()
    SavedJobs.query.delete()
    AppliedJobs.query.delete()
    Salaries.query.delete()
    CompanyReviews.query.delete()
    Companies.query.delete()

    print("Adding data...")
    db.session.add_all(fake.users)
    db.session.add_all(fake.jobs)
    db.session.add_all(fake.saved_jobs)
    db.session.add_all(fake.applied_jobs)
    db.session.add_all(fake.salaries)
    db.session.add_all(fake.company_reviews)
    db.session.add_all(fake.companies)
    db.session.commit()


    print("Committing data...")
    db.session.commit()

    print("Seeding complete!")




# Run this file by typing `python seed.py` in your terminal
# You only need to run this file once to seed your database
# Each time you run this file, it will delete any existing rows
# and add 100 new rows
# You can run this file as many times as you want
# without having duplicate entries in your database
# You can also run this file after you have already started
# your server
# You will need to restart your server if you make changes
# to this file
# You can check the seed file to see what data is being created
# and how the data is related
# You can also check the models.py file to see what tables
# and columns you have in your database
