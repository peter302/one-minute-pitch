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



#Route for adding a new pitch
@main.route('/category/new-pitch/<int:id>', methods=['GET', 'POST'])
@login_required
def new_pitch(id):
    ''' Function to check Pitches form and fetch data from the fields '''
    form = PitchForm()
    category = PitchCategory.query.filter_by(id=id).first()

    if category is None:
        abort(404)

    if form.validate_on_submit():
        content = form.content.data
        new_pitch= Pitch(content=content,category_id= category.id,user_id=current_user.id)
        new_pitch.save_pitch()
        return redirect(url_for('.category', id=category.id))

    return render_template('new_pitch.html', pitch_form=form, category=category)
    
