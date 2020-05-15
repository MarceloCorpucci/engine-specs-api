from api.profile.base import Config


class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_DB = 'dev_engine-specs'
    MONGODB_HOST = 'mongodb://mongo-server/' + MONGODB_DB
