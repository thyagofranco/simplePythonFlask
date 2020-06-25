from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config.from_pyfile('_config.py')
#db = SQLAlchemy(app)

Base = declarative_base()
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

from project.users.views import users_blueprint
from project.courses.views import courses_blueprint


app.register_blueprint(users_blueprint)
app.register_blueprint(courses_blueprint)
