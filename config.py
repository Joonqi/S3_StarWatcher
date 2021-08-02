import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    
    # SQLALCHEMY_DATABASE_URL = os.environ['DATABASE_URL']

class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = '51daa2f796d1167916c3348865ed4175d80087fcac50255f33907f5fd7da6ea9'
    SQLALCHEMY_DATABASE_URI = 'postgresql://fmjxhhfddaofdq:51daa2f796d1167916c3348865ed4175d80087fcac50255f33907f5fd7da6ea9@ec2-44-194-145-230.compute-1.amazonaws.com:5432/d6lbt10a3usids'

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SECRET_KEY = 'qwerqwer'
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:qwerqwer@localhost:5432/watchapp"

class TestingConfig(Config):
    TESTING = True