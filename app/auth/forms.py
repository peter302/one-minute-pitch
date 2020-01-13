from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,ValidationError,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User


class RegistrationForm(FlaskForm):
    '''a form for registering a new user'''
    email=StringField('your email address',validators=[Required(),Email()])
    username=StringField('your username here',validators=[Required()])
    password=PasswordField('password',validators=[Required(),EqualTo('password',message='ensure passwords match')])
    password_confirm=PasswordField('confirm password',validators=[Required()])
    submit=Submited('sign up')
    
