from flask import Flask
from flask_jwt_extended import JWTManager
from api.model.engine_model import db
# from flasgger import Swagger
from flask_swagger_ui import get_swaggerui_blueprint
from api.profile import prod, dev, test
from api.routes.engine_routes import ng_api
from api.routes.warning_preset_routes import wp_api
from api.routes.user_routes import usr_api
from api.routes.injection_map_routes import im_api
from api.routes.ecu_routes import ecu_api


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
    app.register_blueprint(ng_api)
    app.register_blueprint(wp_api)
    app.register_blueprint(im_api)
    app.register_blueprint(ecu_api)
    # swagger = Swagger(app)

    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Engine-Specs-API"
        }
    )
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

    app.debug = True

    return app

