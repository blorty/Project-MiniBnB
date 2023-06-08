# Standard library imports
from os import environ 
from dotenv import load_dotenv

# Remote library imports
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Local imports

# Instantiate app, set attributes
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# Define metadata, instantiate db
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db = SQLAlchemy(metadata=metadata)
migrate = Migrate(app, db)
db.init_app(app)

# Instantiate REST API
api = Api(app)

# Instantiate CORS
CORS(app)

# Load environment variables
load_dotenv('.env')
app.secret_key = environ.get('SECRET_KEY')
app.config['SECRET_KEY'] = app.secret_key
client_id = environ.get('CLIENT_ID')
app.config['CLIENT_ID'] = client_id
client_secret = environ.get('CLIENT_SECRET')
app.config['CLIENT_SECRET'] = client_secret
redirect_uri = environ.get('REDIRECT_URI')
app.config['REDIRECT_URI'] = redirect_uri


