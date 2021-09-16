import os


class Config(object):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', '')


class ProductionConfig(Config):
    TESTING = False


class TestConfig(Config):
    pass
