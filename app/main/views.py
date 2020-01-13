from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User,Pitch,Comments,PitchCategory,Votes
from .. import db
from . forms import PitchForm, CommentForm, CategoryForm
from flask_login import login_required,current_user


#display categories on the landing page
@main.route('/')
def index():
    """ View root page function that returns index page """

    category = PitchCategory.get_categories()

    title = 'Home- Welcome'
    return render_template('index.html', title = title, categories=category)
