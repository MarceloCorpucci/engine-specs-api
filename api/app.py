import os
from flask import Flask, Blueprint, request, jsonify, make_response
from api.model.engine_model import db
import mongoengine
import bson
from flask_marshmallow import Marshmallow
from flasgger import Swagger
from api.profile import prod, dev, test
from api.routes.routes import bp_api


app = Flask(__name__)


def create_app(profile):
    if profile == 'PROD':
        config = prod.ProductionConfig
        # mongoengine.connect(app_config.MONGODB_DB)

    elif profile == 'DEV':
        config = dev.DevelopmentConfig
        # mongoengine.connect(app_config.MONGODB_DB)

    else:
        config = test.TestingConfig
        # mongoengine.connect(app_config.MONGODB_DB, app_config.MONGODB_HOST, alias='mock')

    # app.config.from_object(app_config)
    app.config['MONGODB_SETTINGS'] = {
        'db': config.MONGODB_DB,
        'host': config.MONGODB_HOST
    }

    db.init_app(app)
    app.register_blueprint(bp_api)

    return app


# if os.environ.get('PROFILE') == 'PROD':
#     app_config = prod.ProductionConfig
#
# elif os.environ.get('PROFILE') == 'TEST':
#     app_config = test.TestingConfig
#
# else:
#     app_config = dev.DevelopmentConfig
#
# app.config.from_object(app_config)

# db = MongoEngine(app)

ma = Marshmallow(app)

swagger = Swagger(app)

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")

