from models import db, User, Job, Company
from flask import Flask
from random import randint
from faker import Faker
from flask_bcrypt import Bcrypt
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workwander.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

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
            salary=fake.random_int(),
            user_id=randint(1, 100)
        )
        db.session.add(job)

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
