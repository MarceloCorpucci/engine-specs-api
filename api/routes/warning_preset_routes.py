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


wp_api = Blueprint('wp_api', __name__, url_prefix='/api/warning_presets')


@wp_api.route('/warning_preset', methods=['POST'])
@jwt_required
def create_warning_preset():
    data = request.get_json()
    logging.info('create_warning_preset() --> Received data: ' + str(data))

    try:
        # json_data = json.loads(str(data).replace('\'', '\"'))

        warn_preset_to_save = WarningPreset(name=data['name'],
                                            ect_warning=data['ect_warning'],
                                            oil_temp_warning=data['oil_temp_warning'],
                                            rpm_warning=data['rpm_warning'])
        warn_preset_to_save.engine = Engine.objects.get(model=data['engine']['model'])
        warn_preset_to_save.save()

    except ValidationError as e:
        logging.error(e.errors)
        abort(400)

    logging.info('Saved warning_preset --> ' + str(warn_preset_to_save))

    return make_response(jsonify({'warning_preset': data}), 201)


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


@wp_api.route('/warning_preset/<warning_preset_id>', methods=['DELETE'])
@jwt_required
def delete_warning_preset(warning_preset_id):
    bi = bson.objectid.ObjectId(warning_preset_id)
    WarningPreset.objects.get(id=bi).delete()

    return make_response('', 204)
