from flask import Blueprint, request, abort, jsonify, make_response
import bson
from api.models.users import User
from flask_jwt_extended import create_access_token
from api.utils.responses import response_with
from api.utils import responses as resp
import logging
import json


logging.basicConfig(level=logging.INFO)


usr_api = Blueprint('user_routes', __name__, url_prefix='/api/users')


@usr_api.route('/', methods=['POST'])
def create_user():
    try:
        request_data = request.get_json()
        request_data['password'] = User.generate_hash(request_data['password'])

        user = User()
        user.save()

        return response_with(resp.SUCCESS_201)

    except Exception as e:
        logging.error(e)
        return response_with(resp.INVALID_INPUT_422)
