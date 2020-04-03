from flask import Blueprint, request, abort, jsonify, make_response
from flask_jwt_extended import jwt_required
import bson
from mongoengine import ValidationError
from api.model.ecu_model import Ecu
from api.model.user_model import User
from api.model.injection_map_model import InjectionMap
from flasgger import swag_from
from api.utils.responses import response_with
from api.utils import responses as resp
import logging
import json


logging.basicConfig(level=logging.INFO)


im_api = Blueprint('im_api', __name__, url_prefix='/api/injection_map')


@im_api.route('/', methods=['POST'])
@jwt_required
def create_injection_map():
    try:
        data = request.get_json()
        logging.info('create_injection_map() --> Received data: ' + str(data))
        json_data = json.loads(str(data).replace('\'', '\"'))

        map_to_save = InjectionMap(map=json_data['map'],
                                   date=json_data['date'])
        map_to_save.ecu = Ecu.objects.get(model=json_data['ecu']['model'])
        map_to_save.user = User.objects.get(email=json_data['user']['email'])
        map_to_save.save()

        return response_with(resp.SUCCESS_201)

    except Exception as e:
        logging.error(e)
        return response_with(resp.INVALID_INPUT_422)


@im_api.route('/', methods=['GET'])
def get_injection_map():
    injection_map = InjectionMap.objects.all()
    logging.info('get_injection_map() --> Retrieving data: ' + str(injection_map))

    return make_response(jsonify({'injection_map': injection_map}))


@im_api.route('/ecu/<ecu_model>', methods=['GET'])
def get_injection_map_by_ecu(ecu_model):
    ecu = Ecu.objects.get(model=ecu_model)
    injection_map = InjectionMap.objects.get(ecu=ecu)
    logging.info('get_injection_map_by_ecu() --> Retrieving data: ' + str(injection_map))

    return make_response(jsonify({'injection_map': injection_map}))


@im_api.route('/<injection_map_id>', methods=['DELETE'])
@jwt_required
def delete_injection_map(injection_map_id):
    bi = bson.objectid.ObjectId(injection_map_id)
    InjectionMap.objects.get(id=bi).delete()

    return make_response('', 204)
