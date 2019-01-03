
"""
This module sets the configurations for the application
"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """
    Parent configuration class
    """
    DEBUG = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    CSRF_ENABLED = True

class DevelopmentConfig(Config):
    """Development configurations"""
    DEBUG = True

class TestingConfig(Config):
    """Testing configurations"""
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

class ReleaseConfig(Config):
    """Release configurations"""
    TESTING = False
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'release': ReleaseConfig,
    'default': DevelopmentConfig
}