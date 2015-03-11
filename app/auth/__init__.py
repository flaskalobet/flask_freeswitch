from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
@auth.app_context_processor
def inject_permissions():
    return dic(Permission=Permission)
