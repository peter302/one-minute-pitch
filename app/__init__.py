from flask import flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import flask_sqlalchemy
from flas_login import loginManager



bootstrap=Bootstrap()
db=SQLAlchemy()
login_manager=loginManager()
