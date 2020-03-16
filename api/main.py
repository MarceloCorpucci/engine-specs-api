from flask import Flask
from api.model.engine_model import db
from api.model.authentication_model import User, Role
from flask_security import Security, MongoEngineUserDatastore
from flasgger import Swagger
from api.profile import prod, dev, test
from api.routes.routes import bp_api
from api.utils.responses import response_with
import api.utils.responses as resp


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

    db.init_app(app)
    user_datastore = MongoEngineUserDatastore(db, User, Role)
    security = Security(app, user_datastore)
    app.register_blueprint(bp_api)
    swagger = Swagger(app)

    app.debug = True

    return app

