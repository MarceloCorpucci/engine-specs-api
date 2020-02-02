from api.app import app
from api.routes.routes import bp_api


app.register_blueprint(bp_api)


if __name__ == "__main__":
    app.run(debug=True)
