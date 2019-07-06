import os
import logging
import coloredlogs

from flask import Flask, render_template
from flasgger import Swagger


# Initialize Logger
logger = logging.getLogger('flask')
if not logger.handlers:
    coloredlogs.install(fmt='%(message)s')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(asctime)s | %(levelname)s] %(message)s')
    # ch = logging.StreamHandler()
    # ch.setLevel(logging.DEBUG)
    # ch.setFormatter(formatter)
    # logger.addHandler(ch)


def get_app(profile=None):

    # Flask Application
    app = Flask(__name__,
                static_url_path='/static',
                static_folder='static',
                template_folder='templates'
                )

    # Swagger
    _ = Swagger(app)

    if hasattr(get_app, 'app_singleton') and get_app.app_singleton is not None:
        return get_app.app_singleton

    # Profile
    if profile is None:
        profile = os.environ.get('FLASK_ENV', 'development')

    if profile == 'development':
        app.config.from_object('config.DevelopmentConfig')
    elif profile == 'test':
        app.config.from_object('config.DevelopmentConfig')
    elif profile == 'production':
        app.config.from_object('config.ProductionConfig')
    else:
        raise NotImplementedError('profile ({0}) is not implemented'.format(profile))

    app.url_map.strict_slashes = False

    # Blueprints
    from api.healthz import healthz

    app.register_blueprint(healthz)

    for rule in app.url_map.iter_rules():
        logger.info("%s, %s", rule.methods, rule)

    #
    @app.route("/")
    def index():
        return render_template("index.html")

    # Finish
    get_app.app_singleton = app
    return app

if __name__ == '__main__':
    flask_mode = os.environ.get('FLASK_ENV', 'development')

    app = get_app()
    app.run(
        debug=True,
        use_reloader=True,
        host='0.0.0.0',
        port='5000')




