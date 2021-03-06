from flask import Blueprint, request, abort, jsonify, make_response
from flask_jwt_extended import jwt_required
import bson
from mongoengine import ValidationError
from api.model.ecu_model import Ecu
from api.model.user_model import User
from api.model.injection_map_model import InjectionMap
# from flasgger import swag_from
from api.utils.responses import response_with
from api.utils import responses as resp
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)


im_api = Blueprint('im_api', __name__, url_prefix='/api/injection_maps')


@im_api.route('/injection_map', methods=['POST'])
@jwt_required
def create_injection_map():
    try:
        data = request.get_json()
        logging.info('create_injection_map() --> Received data: ' + str(data))

        map_to_save = InjectionMap(map=data['map'],
                                   date=data['date'])
        map_to_save.ecu = Ecu.objects.get(model=data['ecu']['model'])
        map_to_save.user = User.objects.get(email=data['user']['email'])
        map_to_save.save()

    except Exception as e:
        logging.error(e)
        return response_with(resp.INVALID_INPUT_422)

    saved_record = InjectionMap.objects.get(ecu=map_to_save.ecu)
    logging.info('Saved Injection Map --> ' + str(saved_record))

    return make_response(jsonify({'injection_map': saved_record}), 201)


@im_api.route('/', methods=['GET'])
def get_injection_map():
    injection_map = InjectionMap.objects.all()
    logging.info('get_injection_map() --> Retrieving data: ' + str(injection_map))

    return make_response(jsonify({'injection_map': injection_map}))


@im_api.route('/injection_map/<injection_map_id>', methods=['GET'])
def get_injection_map_by_id(injection_map_id):
    bi = bson.objectid.ObjectId(injection_map_id)
    injection_map = InjectionMap.objects.get(id=bi)
    injection_map.date = datetime.strptime(str(injection_map.date), "%Y-%m-%d %H:%M:%S")
    logging.info('get_injection_map_by_id() --> Retrieving data: ' + str(injection_map))

    return make_response(jsonify({'injection_map': injection_map}))


@im_api.route('/ecu/<ecu_model>', methods=['GET'])
def get_injection_map_by_ecu(ecu_model):
    ecu = Ecu.objects.get(model=ecu_model)
    injection_map = InjectionMap.objects.get(ecu=ecu)
    injection_map.date = datetime.strptime(str(injection_map.date), "%Y-%m-%d %H:%M:%S")
    logging.info('get_injection_map_by_ecu() --> Retrieving data: ' + str(injection_map))

    return make_response(jsonify({'injection_map': injection_map}))


@im_api.route('/injection_map/<injection_map_id>', methods=['DELETE'])
@jwt_required
def delete_injection_map(injection_map_id):
    bi = bson.objectid.ObjectId(injection_map_id)
    InjectionMap.objects.get(id=bi).delete()

    return make_response('', 204)


@im_api.route('/ecu/<ecu_model>', methods=['DELETE'])
@jwt_required
def delete_injection_map_by_ecu_model(ecu_model):
    ecu = Ecu.objects.get(model=ecu_model)
    InjectionMap.objects.get(ecu=ecu).delete()

    return make_response('', 204)

