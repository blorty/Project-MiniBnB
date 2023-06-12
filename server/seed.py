from flask import Flask
from flask_migrate import Migrate
from models import db, User, Job, AppliedJob, Salary, CompanyReview, Company
from config import app
from random import randint
from faker import Faker
from flask_bcrypt import Bcrypt
from datetime import date

migrate = Migrate(app, db)

with app.app_context():
    print("Deleting data...")
    db.drop_all()

    print("Creating tables...")
    db.create_all()

    fake = Faker()

    for _ in range(5, 21):
        user = User()
        user.username = fake.name()
        user.email = fake.email()
        user._password_hash = fake.password()
        db.session.add(user)

    db.session.commit()

    for _ in range(100):
        job = Job(
        title=fake.job(),
        description=fake.text(),
        location=fake.city(),
        salary=fake.random_int(),
        User_id=randint(1, 100)
    )
    db.session.add(job)

    db.session.commit()


    for _ in range(100):
        applied_job = AppliedJob(
            user_id=randint(1, 100),
            job_id=randint(1, 100),
            salary=fake.random_int(),
            company_review=fake.text(),
            applied_date=date.today()

    )
    db.session.add(applied_job)

    db.session.commit()

    for _ in range(100):
        salary = Salary(
            salary=fake.random_int(),
            User_id=randint(1, 100)
        )
    db.session.add(salary)

    db.session.commit()
    for _ in range(100):
        company_review = CompanyReview(
            review=fake.text(),
            User_id=randint(1, 100),
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



