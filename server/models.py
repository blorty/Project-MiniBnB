from sqlalchemy_serializer import SerializerMixin

from config import db

# Models go here!

class User(db.Model, SerializerMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)


class Recipe(db.Model, SerializerMixin):
    __tablename__ = 'recipe'
    id = db.Column(db.Integer, primary_key=True)
