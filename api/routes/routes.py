from flask import Blueprint, request, abort, jsonify, make_response
from flask_jwt_extended import jwt_required
import bson
from mongoengine import ValidationError
from api.model.engine_model import Engine
from api.model.warning_preset_model import WarningPreset
from flasgger import swag_from
import logging
import json


logging.basicConfig(level=logging.INFO)


bp_api = Blueprint('api', __name__, url_prefix='/api')


@bp_api.route('/engine', methods=['POST'])
@jwt_required
@swag_from('create_engine.yml')
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


@bp_api.route('/engines', methods=['GET'])
@swag_from('engines.yml')
def get_engines():
    engines = Engine.objects.all()
    logging.info('get_engines() --> Retrieving data: ' + str(engines))

    return make_response(jsonify({'engines': engines}))


@bp_api.route('/engine/<engine_id>', methods=['GET'])
@swag_from('engine.yml')
def get_engine_id(engine_id):
    bi = bson.objectid.ObjectId(engine_id)
    engine = Engine.objects.get(id=bi)
    logging.info('get_engine_id() --> Retrieving data: ' + str(engine))

    return make_response(jsonify({'engine': engine}))


@bp_api.route('/engine/<model>', methods=['GET'])
def get_engine(model):
    engine = Engine.objects.get(model=model)
    logging.info('get_engine() --> Retrieving data: ' + str(engine))

    return make_response(jsonify({'engine': engine}))


@bp_api.route('/engine/<engine_id>', methods=['DELETE'])
def delete_engine(engine_id):
    bi = bson.objectid.ObjectId(engine_id)
    Engine.objects.get(id=bi).delete()

    return make_response('', 204)


@bp_api.route('/warning_preset', methods=['POST'])
def create_warning_preset():
    data = request.get_json()
    logging.info('create_warning_preset() --> Received data: ' + str(data))

    try:
        json_data = json.loads(str(data).replace('\'', '\"'))

        warn_preset_to_save = WarningPreset(ect_warning=json_data['ect_warning'],
                                            oil_temp_warning=json_data['oil_temp_warning'],
                                            rpm_warning=json_data['rpm_warning'])
        warn_preset_to_save.engine = Engine.objects.get(model=json_data['engine']['model'])
        warn_preset_to_save.save()

    except ValidationError as e:
        logging.error(e.errors)
        abort(400)

    logging.info('Saved engine --> ' + str(warn_preset_to_save))

    return make_response(jsonify({'warning_preset': data}), 201)


@bp_api.route('/warning_presets', methods=['GET'])
def get_warning_presets():
    warn_presets = WarningPreset.objects.all()
    logging.info('get_warning_presets() --> Retrieving data: ' + str(warn_presets))

    return make_response(jsonify({'warn_presets': warn_presets}))


@bp_api.route('/warning_preset/<warning_preset_id>', methods=['GET'])
def get_warning_preset(warning_preset_id):
    bi = bson.objectid.ObjectId(warning_preset_id)
    warn_preset = WarningPreset.objects.get(id=bi)
    logging.info('get_warning_preset() --> Retrieving data: ' + str(warn_preset))

    return make_response(jsonify({'warning_preset': warn_preset}))


@bp_api.route('/warning_preset/<warning_preset_id>', methods=['DELETE'])
def delete_warning_preset(warning_preset_id):
    bi = bson.objectid.ObjectId(warning_preset_id)
    WarningPreset.objects.get(id=bi).delete()

    return make_response('', 204)
