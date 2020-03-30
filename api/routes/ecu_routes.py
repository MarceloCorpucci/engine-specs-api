from flask import Blueprint, request, abort, jsonify, make_response
from flask_jwt_extended import jwt_required
import bson
from mongoengine import ValidationError
from api.model.ecu_model import Ecu
from api.model.engine_model import Engine
from api.model.warning_preset_model import WarningPreset
from api.model.user_model import User
from flasgger import swag_from
from api.utils.responses import response_with
from api.utils import responses as resp
import logging
import json

logging.basicConfig(level=logging.INFO)

ecu_api = Blueprint('ecu_api', __name__, url_prefix='/api/ecu')


@ecu_api.route('/', methods=['POST'])
@jwt_required
def create_ecu():
	try:
		data = request.get_json()
		logging.info('create_ecu() --> Received data: ' + str(data))
		json_data = json.loads(str(data).replace('\'', '\"'))

		ecu_to_save = Ecu(model=json_data['model'],
						  firmware=json_data['firmware'],
						  date_added=json_data['date_added'])

		ecu_to_save.engine = Engine.objects.get(model=json_data['engine']['model'])
		ecu_to_save.warning_preset = WarningPreset.objects.get(???=json_data['warning_preset']['???'])
		ecu_to_save.user = User.objects.get(email=json_data['user']['email'])

		ecu_to_save.save()

		return response_with(resp.SUCCESS_201)

	except Exception as e:
		logging.error(e)
		return response_with(resp.INVALID_INPUT_422)
