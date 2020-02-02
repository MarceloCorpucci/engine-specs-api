from flask import Flask, Blueprint, request, jsonify, make_response
from flask_mongoengine import MongoEngine
import bson
from flask_marshmallow import Marshmallow
from flasgger import Swagger


app = Flask(__name__)

app.config['MONGODB_DB'] = 'engine-specs'
db = MongoEngine(app)

ma = Marshmallow(app)

swagger = Swagger(app)
