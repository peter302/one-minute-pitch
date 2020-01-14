from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,ValidationError,BooleanField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User


class RegistrationForm(FlaskForm):
    '''a form for registering a new user'''
    email=StringField('your email address',validators=[Required(),Email()])
    username=StringField('your username here',validators=[Required()])
    password=PasswordField('password',validators=[Required(),EqualTo('password',message='ensure passwords match')])
    password_confirm=PasswordField('confirm password',validators=[Required()])
    submit=SubmitField('sign up')

#custom validators
    def validate_email(self,data_field):
        ''' a function that validates email'''
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('that email is already registred')

    def validate_username(self,data_field):
        ''' a function that is checking that the new user doesnt use an already registred username'''
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('that username alreadyexists')


#login class to log in users
class LoginForm(FlaskForm):
    email=StringField('email address',validators=[Required(),Email()])
    password=PasswordField('password',validators=[Required()])
    remember=BooleanField('remember me')
    submit=SubmitField('sign in')
