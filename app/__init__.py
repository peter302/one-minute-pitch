from flask import flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import flask_sqlalchemy
from flas_login import loginManager



bootstrap=Bootstrap()
db=SQLAlchemy()
login_manager=loginManager()


def create_app(config_name):
    app=Flask(__name__)
    # create the app configurations.
    app.config.from_object(config_options[config_name])

    #initializing flask extentions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.session_protection='strong'
    login_manager.login_view='auth.login'

    #registering the blueprint
    from .main import main as main_blueprint
    
