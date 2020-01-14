from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from sqlalchemy.sql import func


@login_manager.user_loader
def load_user(user_id):
    '''
    a function to load users'
    '''
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    """ class modelling the users """

    __tablename__='users'

    #create the columns
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index =True)
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship("Pitch", backref="user", lazy = "dynamic")
    comment = db.relationship("Comments", backref="user", lazy = "dynamic")
    vote = db.relationship("Votes", backref="user", lazy = "dynamic")    
