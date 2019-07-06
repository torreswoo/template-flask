import os

from flasgger import swag_from
from flask import Blueprint, request, jsonify, session
from app import get_app

healthz = Blueprint('healthz', __name__, url_prefix='/healthz')

@healthz.route('/', methods=['GET'])
@swag_from('apidoc/healthz.yaml')
def get_healthz():
    app = get_app()

    flask_mode = os.environ.get('FLASK_ENV', 'development')

    return jsonify(
        {
            'profile' : f'{flask_mode}',
            'debug' : f'{app.debug}',
            'app_env' : f'{app.config["ENV"]}'
        }
    )

@healthz.route('/error', methods=['GET'])
@swag_from('apidoc/healthz_error.yaml')
def hello_error():
    raise ItIsNotError('This is intended error for testing sentry.')


class ItIsNotError(Exception):
    pass