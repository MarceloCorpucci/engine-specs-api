from flask import Blueprint, request, abort, jsonify, make_response
from flask_jwt_extended import jwt_required
import bson
from mongoengine import ValidationError
from api.model.engine_model import Engine
import logging


logging.basicConfig(level=logging.INFO)


ng_api = Blueprint('ng_api', __name__, url_prefix='/api/engines')


@ng_api.route('/', methods=['GET'])
def get_engines():
    engines = Engine.objects.all()
    logging.info('get_engines() --> Retrieving data: ' + str(engines))

    return make_response(jsonify({'engines': engines}))


@ng_api.route('/engine', methods=['POST'])
@jwt_required
def create_engine():
    data = request.get_json()
    try:
        logging.info('create_engine() --> Received data: ' + str(data))

        engine = Engine(**data)
        engine.save()

    except ValidationError as e:
        logging.error(e.errors)
        abort(400)

    saved_engine = Engine.objects.get(model=data['model'])
    logging.info('Saved engine --> ' + str(saved_engine))

    return make_response(jsonify({'engine': saved_engine}), 201)


@ng_api.route('/engine/<engine_id>', methods=['GET'])
def get_engine_id(engine_id):
    bi = bson.objectid.ObjectId(engine_id)
    engine = Engine.objects.get(id=bi)
    logging.info('get_engine_id() --> Retrieving data: ' + str(engine))

    return make_response(jsonify({'engine': engine}))


@ng_api.route('/engine/<engine_id>', methods=['DELETE'])
@jwt_required
def delete_engine(engine_id):
    bi = bson.objectid.ObjectId(engine_id)
    Engine.objects.get(id=bi).delete()

    return make_response('', 204)


@ng_api.route('/model/<model>', methods=['GET'])
def get_engine(model):
    engine = Engine.objects.get(model=model)
    logging.info('get_engine() --> Retrieving data: ' + str(engine))

    return make_response(jsonify({'engine': engine}))
