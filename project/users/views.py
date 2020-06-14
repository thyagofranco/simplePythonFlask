

from flask import redirect , render_template, request, session, flash, url_for, Blueprint


users_blueprint = Blueprint("users", __name__)


@users_blueprint.route('/', methods=['GET','POST'])
def login():
    error = None
    return render_template('login.html', error=error)
