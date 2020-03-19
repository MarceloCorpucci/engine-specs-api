from flask import Flask
from flask_jwt_extended import JWTManager
from api.model.engine_model import db
from flasgger import Swagger
from api.profile import prod, dev, test
from api.routes.routes import bp_api
from api.routes.user_routes import usr_api


def create_app(profile):
    app = Flask(__name__)

    if profile == 'PROD':
        config = prod.ProductionConfig

    elif profile == 'DEV':
        config = dev.DevelopmentConfig

    else:
        config = test.TestingConfig

    app.config['MONGODB_SETTINGS'] = {
        'db': config.MONGODB_DB,
        'host': config.MONGODB_HOST
    }

    app.config['JWT_SECRET_KEY'] = 'super-secret'
    jwt = JWTManager(app)
    db.init_app(app)
    app.register_blueprint(usr_api)
    app.register_blueprint(bp_api)
    swagger = Swagger(app)

    app.debug = True

    return app

