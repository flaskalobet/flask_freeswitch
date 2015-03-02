from flask import Blueprint

auth = Blueprint('freeswitch', __name__)

from . import views
