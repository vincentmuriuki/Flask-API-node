import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True
    TESTING = True
    CSRF_ENABLED = True

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True

class TestingConfig(Config):
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

class ReleaseConfig(Config)
    TESTING = False
    DEBUG = False

config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "release": ReleaseConfig,
    "default": DevelopmentConfig
}