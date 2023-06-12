from flask import Flask
from flask_migrate import Migrate
from models import db, User, Job, Company
from random import randint
from faker import Faker
from app import app
from datetime import date




# Instantiate REST API

migrate = Migrate(app, db)

with app.app_context():
    print("Deleting data...")
    db.drop_all()

    print("Creating tables...")
    db.create_all()

    fake = Faker()

    for _ in range(5, 21):
        user = User()
        user.username = fake.user_name()
        user.email = fake.email()
        user._password_hash = fake.password()
        db.session.add(user)

    db.session.commit()

    for _ in range(100):
        job = Job(
            title=fake.job(),
            description=fake.text(),
            location=fake.city(),
            salary=fake.random_int(min=50000, max=100000),
            user_id=randint(1, 100)
        )
        db.session.add(job)

    db.session.commit()

    for _ in range(100):
        company = Company(
            name=fake.company(),
            industry=fake.job(),
            website=fake.url()
        )
        db.session.add(company)

    db.session.commit()

print("Seeding complete!")