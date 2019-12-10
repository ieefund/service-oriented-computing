import logging
import os

# from firebase import firebase
from flask import Flask, render_template, request, redirect
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from database import base
from database.base import User
from views.menus import menus_blueprint
from rest_server.resource import TemperatureResource, TemperatureCreationResource, TemperatureByLocationResource
from rest_server.resource_check import resource_blueprint
from views.auth import auth_blueprint, kakao_oauth
from flask_login import current_user, LoginManager

application = Flask(__name__)
application.register_blueprint(resource_blueprint, url_prefix="/resource")
application.register_blueprint(menus_blueprint, url_prefix="/menus")
application.register_blueprint(auth_blueprint, url_prefix="/auth")
# application.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///database.comment.db'
# application.config['SECRET_KEY'] = "random string"
#
# db = SQLAlchemy(application)

# firebase = \
#     firebase.FirebaseApplication('https://fiery-torch-8827.firebaseio.com', None)
logging.basicConfig(filename='test.log')

api = Api(application)
api.add_resource(TemperatureResource, "/resource/<sensor_id>")
api.add_resource(TemperatureCreationResource, "/resource/resource_creation")
api.add_resource(TemperatureByLocationResource, "/resource/location/<location>")

application.config['WTF_CSRF_SECRET_KEY'] = os.urandom(24)
application.config['SECRET_KEY'] = os.urandom(24)

login_manager = LoginManager()
login_manager.init_app(application)

def __init__(comment):
    self.comment = comment;

@login_manager.user_loader
def load_user(user_id):
    q = base.db_session.query(User).filter(User.id == user_id)
    user = q.first()

    if user is not None:
        user._authenticated = True
    return user


@application.route('/')
def hello_html():
    # html file은 templates 폴더에 위치해야 함

    return render_template(
        'index.html',
        nav_menu="home",
        current_user=current_user,
        kakao_oauth=kakao_oauth
    )

@application.route('/login', methods = ['POST', 'GET'])
def success():
    if request.method == 'POST':
        myName = request.form['myName']
    else:
        myName = request.args.get('myName')

    return 'welcome {0}'.format(myName)

@application.errorhandler(404)
def page_not_found(error):
    return "<h1>404 Error</h1>", 404

@application.before_request
def before_request():
    logging.info("before_request")

# @application.route('/')
# def showComment():
#     return render_template('img.html', comment=comment.query.all())

@application.route('/img')
def img():

    return render_template(
        'img.html', kakao_oauth=kakao_oauth
    )

@application.route('/messages')
def messages():
    # result = firebase.get('/messages', None)
    return render_template('img.html', messages=result)

@application.route('/submit_message', methods=['GET', 'POST'])
def submit_message():
    message = {
        'body': request.form['message']
    }
    # firebase.post('/messages', message)
    return redirect('/img')


if __name__ == '__main__':
    logging.info("flask web server started!!")
    application.debug = True
    application.config['DEBUG'] = True
    application.run(host="localhost", port="8080")
