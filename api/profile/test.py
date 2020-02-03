from api.profile.base import Config


class TestingConfig(Config):
    TESTING = True
    MONGODB_DB = 'mocked_engine-specs'
    MONGODB_HOST = 'mongomock://localhost'

