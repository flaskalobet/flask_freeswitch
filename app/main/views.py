from flask import render_template, session, redirect, url_for
from . import main

from .forms import NameForm

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = NameForm()
    name = None
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('login.html', form=form, name=name)
