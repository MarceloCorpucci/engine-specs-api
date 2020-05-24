from flask import Blueprint, request, abort, jsonify, make_response
from flask_jwt_extended import jwt_required
import bson
from mongoengine import ValidationError
from api.model.engine_model import Engine
from api.model.warning_preset_model import WarningPreset
# from flasgger import swag_from
import logging
import json


logging.basicConfig(level=logging.INFO)


wp_api = Blueprint('wp_api', __name__, url_prefix='/api/warning_presets')


@wp_api.route('/warning_preset', methods=['POST'])
@jwt_required
def create_warning_preset():
    data = request.get_json()
    logging.info('create_warning_preset() --> Received data: ' + str(data))

    try:
        warn_preset_to_save = WarningPreset(name=data['name'],
                                            ect_warning=data['ect_warning'],
                                            oil_temp_warning=data['oil_temp_warning'],
                                            rpm_warning=data['rpm_warning'])
        warn_preset_to_save.engine = Engine.objects.get(model=data['engine']['model'])
        warn_preset_to_save.save()

    except ValidationError as e:
        logging.error(e.errors)
        abort(400)

    saved_record = WarningPreset.objects.get(name=data['name'])
    logging.info('Saved warning_preset --> ' + str(saved_record))

    return make_response(jsonify({'warning_preset': saved_record}), 201)


@wp_api.route('/', methods=['GET'])
def get_warning_presets():
    warn_presets = WarningPreset.objects.all()
    logging.info('get_warning_presets() --> Retrieving data: ' + str(warn_presets))

    return make_response(jsonify({'warn_presets': warn_presets}))


@wp_api.route('/warning_preset/<warning_preset_id>', methods=['GET'])
def get_warning_preset(warning_preset_id):
    bi = bson.objectid.ObjectId(warning_preset_id)
    warn_preset = WarningPreset.objects.get(id=bi)
    logging.info('get_warning_preset() --> Retrieving data: ' + str(warn_preset))

    return make_response(jsonify({'warning_preset': warn_preset}))


@wp_api.route('/name/<name>', methods=['GET'])
def get_warning_preset_by_name(name):
    warn_preset = WarningPreset.objects.get(name=name)
    logging.info('get_warning_preset() --> Sending data: ' + str(warn_preset))

    return make_response(jsonify({'warning_preset': warn_preset}))


@wp_api.route('/warning_preset/<warning_preset_id>', methods=['DELETE'])
@jwt_required
def delete_warning_preset(warning_preset_id):
    bi = bson.objectid.ObjectId(warning_preset_id)
    WarningPreset.objects.get(id=bi).delete()

    return make_response('', 204)


@wp_api.route('/name/<name>', methods=['DELETE'])
@jwt_required
def delete_warning_preset_by_name(name):
    WarningPreset.objects.get(name=name).delete()

    return make_response('', 204)
