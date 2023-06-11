from flask import Flask
from flask_migrate import Migrate
from models import db, User, Job, AppliedJob, Salary, CompanyReview, Company
from config import app
from random import randint, choice as rc
from faker import Faker

migrate = Migrate(app, db)

with app.app_context():
    print("Deleting data...")
    db.drop_all()

    print("Creating tables...")
    db.create_all()



# Seed data
fake = Faker()

for _ in range(100):
    user = User(
        name=fake.name(),
        email=fake.email(),
        password=fake.password()
    )
    db.session.add(user)

db.session.commit()

for _ in range(100):
    job = Job(
        title=fake.job(),
        description=fake.text(),
        location=fake.city(),
        salary=fake.random_int(),
        user_id=randint(1, 100)
    )
    db.session.add(job)

db.session.commit()

for _ in range(100):
    saved_job = SavedJob(
        user_id=randint(1, 100),
        job_id=randint(1, 100)
    )
    db.session.add(saved_job)

db.session.commit()

for _ in range(100):
    applied_job = AppliedJob(
        user_id=randint(1, 100),
        job_id=randint(1, 100)
    )
    db.session.add(applied_job)

db.session.commit()

for _ in range(100):
    salary = Salary(
        salary=fake.random_int(),
        user_id=randint(1, 100)
    )
    db.session.add(salary)

db.session.commit()

for _ in range(100):
    company_review = CompanyReview(
        review=fake.text(),
        user_id=randint(1, 100),
        company_id=randint(1, 100)
    )
    db.session.add(company_review)

db.session.commit()

for _ in range(100):
    company = Company(
        name=fake.company(),
        description=fake.text(),
        location=fake.city(),
        industry=fake.job(),
        website=fake.url()
    )
    db.session.add(company)

db.session.commit()

print("Seeding complete!")

