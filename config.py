import os
from pathlib import Path
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '0w%tvx4s&$z7a0a&5zz$3a+o$5=9'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    db_name = "flask-example"
    SQLALCHEMY_DATABASE_URI = f"postgresql://conveyor@localhost/{db_name}"


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
