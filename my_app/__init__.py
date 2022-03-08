from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_caching import Cache  # Import Cache from flask_caching module



app = Flask(__name__)
app.config.from_object('config.Docker')

#app.config.from_object('config.DevelopmentConfig')

cache = Cache(app)  # Initialize Cache

db = SQLAlchemy(app)
api = Api(app)

from my_app.catalog.views import catalog
app.register_blueprint(catalog)

db.create_all()
