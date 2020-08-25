from pathlib import Path

import os
import flask
from . import development, testing, production

print("global config/init")
def create_app(config_name='default'):
    print("create_app")
    """Flask app factory

    :config_name: a string object.
    :returns: flask.Flask object

    """
    # Set environment variables
    # TODO: Move these to config files themselves
    # os.environ['OMP_THREAD_LIMIT'] = os.getenv('OMP_THREAD_LIMIT')


    app = flask.Flask(__name__)

    # set the config vars using the config name and current_app
    config[config_name](app)

    register_blueprints(app)

    return app


def register_blueprints(app):
    """Register all blueprints.

    :app: flask.Flask object
    :returns: None

    """
    # app.register_blueprint(users.blueprint)


def set_app_config_keys(app, settings):
    """Load all flask.Flask config vars.

    :app: a flask.Flask object
    :settings: a module with config vars
    :returns: None

    """
    print("set_app_config_keys")
    # create a unique dict with all config vars
    all_config_vars = dict(
        list(settings.FLASK_VARS.items()) +
        list(settings.DB_CONNECTION.items()) +
        list(settings.PATHS.items())
    )

    for key, value in all_config_vars.items():
        app.config[key] = value

    # TODO: Better place to do this?
    # if not (settings.PATHS['IMAGES_ROOT'] and Path(settings.PATHS['IMAGES_ROOT']).exists()):
    #     raise Exception('Images root directory does not exist: %s' % settings.PATHS['IMAGES_ROOT'])
    #

def development_config(app):
    """Call the function responsable by load config vars
    using 'development' settings.

    :app: a flask.Flask object
    :returns: None

    """
    print("development_config")
    set_app_config_keys(app, development)


def testing_config(app):
    """Call the function responsable by load config vars
    using 'testing' settings.

    :app: a flask.Flask object
    :returns: None

    """
    print("testing_config")
    set_app_config_keys(app, testing)


def production_config(app):
    """Call the function responsable by load config vars
    using 'production' settings.

    :app: a flask.Flask object
    :returns: None

    """
    print("production_config")
    set_app_config_keys(app, production)


# Yep, I know I could use lambdas
config = {
    'development': development_config,
    'testing': testing_config,
    'production': production_config,
    'default': development_config,
}