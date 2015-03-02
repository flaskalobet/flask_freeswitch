from flask import render_template
from . import auth


@auth.route('/freeswitch/user')
def login():
        return render_template('freeswitch/user.html')
