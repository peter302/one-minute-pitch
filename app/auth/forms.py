from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,ValidationError,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
