from flask import Blueprint, request, jsonify, make_response
import bson
from api.model.engine_model import Engine
from api.model.warning_preset_model import WarningPreset
from flasgger import swag_from
import logging


logging.basicConfig(level=logging.INFO)


bp_api = Blueprint('api', __name__, url_prefix='/api')


@bp_api.route('/engine', methods=['POST'])
def create_engine():
    data = request.get_json()

    logging.info('create_engine() --> Received data: ' + str(data))

    engine = Engine(**data)
    engine.save()

    saved_engine = Engine.objects.get(model=data['model'])
    logging.info('Saved engine --> ' + str(saved_engine))

    return make_response(jsonify({'engine': saved_engine}), 201)


@bp_api.route('/engines', methods=['GET'])
@swag_from('engines.yml')
def get_engines():
    engines = Engine.objects.all()

    return make_response(jsonify({'engines': engines}))


@bp_api.route('/engine/<id>', methods=['GET'])
def get_engine(id):
    bi = bson.objectid.ObjectId(id)
    engine = Engine.objects.get(id=bi)

    return make_response(jsonify({'engine': engine}))


@bp_api.route('/engine/<id>', methods=['DELETE'])
def delete_engine(id):
    bi = bson.objectid.ObjectId(id)
    Engine.objects.get(id=bi).delete()

    return make_response('', 204)


@bp_api.route('/warning_preset', methods=['POST'])
def create_warning_preset():
    data = request.get_json()

    # logging.info(data)
    # logging.info(data['engine'])

    # engine_to_save = Engine(model=data['engine'][0]['model'],
    #                         displacement=data['engine'][0]['displacement'],
    #                         power=data['engine'][0]['power'],
    #                         forced_induction=data['engine'][0]['forced_induction']
    #                         )
    #
    # warn_preset_to_save = WarningPreset(ect_warning=data['ect_warning'],
    #                                     oil_temp_warning=data['oil_temp_warning'],
    #                                     rpm_warning=data['rpm_warning'])

    # warn_preset_to_save.engine.append(engine_to_save)
    # warn_preset_to_save.save()

    return make_response(jsonify({'warning_preset': data}), 201)
