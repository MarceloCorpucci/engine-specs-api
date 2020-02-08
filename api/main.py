from flask import Flask
from api.model.engine_model import db
from flasgger import Swagger
from api.profile import prod, dev, test
from api.schema.engine_schema import ma
from api.routes.routes import bp_api


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
    app.register_blueprint(bp_api)
    ma.init_app(app)
    swagger = Swagger(app)

    app.debug = True

    return app


# if __name__ == "__main__":
#    app.run(port=5000, host="0.0.0.0", debug=True)

