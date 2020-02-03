from api.profile.base import Config


class ProductionConfig(Config):
    MONGODB_DB = 'engine-specs'
    MONGODB_HOST = 'mongodb://localhost/' + MONGODB_DB


