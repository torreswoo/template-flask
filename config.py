from flask import Config

import os


class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False

    REDIS = {
        'host': os.environ.get('REDIS_HOST', None),
        'port': int(os.environ.get('REDIS_PORT', '6379')),
        'db': os.environ.get('REDIS_DB', None),
        'password': os.environ.get('REDIS_PASSWORD', None),
        'decode_responses': True  # Automatically convert binary string to unicode
    }

    THREADS_PER_PAGE = 2
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = ''
    SECRET_KEY = ''


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    TESTING = True

    REDIS = {
        'host': os.environ.get('REDIS_HOST', None),
        'port': int(os.environ.get('REDIS_PORT', '6379')),
        'db': os.environ.get('REDIS_DB', None),
        'password': os.environ.get('REDIS_PASSWORD', None),
        'decode_responses': True  # Automatically convert binary string to unicode
    }

    THREADS_PER_PAGE = 2
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = ''
    SECRET_KEY = ''


class TestConfig(DevelopmentConfig):
    ENV = 'test'
    TESTING = False

    CSRF_SESSION_KEY = ''
    SECRET_KEY =''