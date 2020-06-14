
from flask import request, redirect, render_template, session, url_for, Blueprint


courses_blueprint = Blueprint("courses",__name__)


#def listCourses():
#    return {'750':{'Linux ':''}}




@courses_blueprint.route('/courses', methods=['GET'])
def courses():
    return render_template('listCourses.html')
