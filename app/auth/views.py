from flask import render_template, redirect, url_for
from . import auth
from .forms import LoginForm
from .models import User
from flask.ext.login import login_user, logout_user, login_required

@auth.route('/auth/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(url_for('main.index'))
            #return render_template('test.html')
    return render_template('auth/login.html', form=form)

@auth.route('/auth/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
