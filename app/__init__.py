from flask import Flask, render_template
from config import config

#use bootstrap extension
from flask.ext.bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    #init bootstrap
    bootstrap.init_app(app)

    # attach routes and custom error pages here
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
