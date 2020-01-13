from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required



class PitchForm(FlaskForm):
    '''
    Class to create a wtf form for creating a pitch
    '''
    content = TextAreaField('YOUR PITCH')
    submit = SubmitField('SUBMIT')


class CommentForm(FlaskForm):
    '''
    Class to create a wtf form for creating a pitch
    '''
    opinion = TextAreaField('WRITE COMMENT')
    submit = SubmitField('SUBMIT')
