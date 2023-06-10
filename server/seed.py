#!/usr/bin/env python3
from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, User, Job, SavedJob, AppliedJob, Salary, CompanyReview, Company
from config import app
from random import randint, choice as rc
from faker import Faker


with app.app_context():
    db.init_app(app)
    db.create_all()

    print("Deleting data...")
    User.query.delete()
    Job.query.delete()
    SavedJob.query.delete()
    AppliedJob.query.delete()
    Salary.query.delete()
    CompanyReview.query.delete()
    Company.query.delete()

    print("Adding data...")
    fake = Faker()
    for i in range(100):
        user = User(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            password=fake.password(),
            phone_number=fake.phone_number(),
            location=fake.city(),
            is_employer=fake.boolean(),
            is_admin=fake.boolean(),
            is_active=fake.boolean(),
            is_anonymous=fake.boolean(),
            is_authenticated=fake.boolean(),
        )
        db.session.add(user)
        db.session.commit()

    for i in range(100):
        job = Job(
            title=fake.job(),
            description=fake.text(),
            location=fake.city(),
            salary=fake.pyint(),
            company_id=randint(1, 100)
        )
        db.session.add(job)
        db.session.commit()

    for i in range(100):
        saved_job = SavedJob(
            user_id=randint(1, 100),
            job_id=randint(1, 100)
        )
        db.session.add(saved_job)
        db.session.commit()

    for i in range(100):
        applied_job = AppliedJob(
            user_id=randint(1, 100),
            job_id=randint(1, 100)
        )
        db.session.add(applied_job)
        db.session.commit()

    for i in range(100):
        salary = Salary(
            salary=fake.pyint(),
            user_id=randint(1, 100)
        )
        db.session.add(salary)
        db.session.commit()

    for i in range(100):
        company_review = CompanyReview(
            review=fake.text(),
            user_id=randint(1, 100),
            company_id=randint(1, 100)
        )
        db.session.add(company_review)
        db.session.commit()

    for i in range(100):
        company = Company(
            name=fake.company(),
            description=fake.text(),
            location=fake.city(),
            industry=fake.job(),
            website=fake.url()
        )
        db.session.add(company)
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
