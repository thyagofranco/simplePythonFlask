from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('_config.py')

from project.users.views import users_blueprint
from project.courses.views import courses_blueprint


app.register_blueprint(users_blueprint)
app.register_blueprint(courses_blueprint)
