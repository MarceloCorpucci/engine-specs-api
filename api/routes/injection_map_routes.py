from flask import Blueprint, request, abort, jsonify, make_response
from flask_jwt_extended import jwt_required
import bson
from mongoengine import ValidationError
from api.model.engine_model import Engine
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
        map_to_save.engine = Engine.objects.get(model=json_data['engine']['model'])
        map_to_save.save()

        return response_with(resp.SUCCESS_201)

    except Exception as e:
        logging.error(e)
        return response_with(resp.INVALID_INPUT_422)

