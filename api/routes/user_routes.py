from flask import Blueprint, request, jsonify, make_response
from api.model.user_model import User
from flask_jwt_extended import create_access_token
from api.utils.responses import response_with
from api.utils import responses as resp
from mongoengine import ValidationError
import bson

import logging


logging.basicConfig(level=logging.INFO)


usr_api = Blueprint('user_routes', __name__, url_prefix='/api/users')


@usr_api.route('/user', methods=['POST'])
def create_user():
    logging.info('create_user()')

    try:
        request_data = request.get_json()
        request_data['password'] = User.generate_hash(request_data['password'])

        user = User(email=request_data['email'], password=request_data['password'])
        user.save()

    except Exception as e:
        logging.error(e)
        return response_with(resp.INVALID_INPUT_422)

    saved_record = User.objects.get(email=request_data['email'])
    logging.info('Saved user --> email: ' + str(saved_record))

    return make_response(jsonify({'user': saved_record}), 201)


@usr_api.route('/login', methods=['POST'])
def authenticate_user():
    try:
        data = request.get_json()
        user = User()
        current_user = user.find_by_email(data['email'])
        if not current_user:
            return response_with(resp.SERVER_ERROR_404)

        if user.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity=data['email'])
            return response_with(resp.SUCCESS_201, value={
                'message': 'Logged in as {}'.format(current_user.email), "access_token": access_token})
        else:
            return response_with(resp.UNAUTHORIZED_401)

    except Exception as e:
        logging.error(e)
        return response_with(resp.INVALID_INPUT_422)


@usr_api.route('/email/<email>', methods=['GET'])
def get_user_by_email(email):
    user = User.objects.get(email=email)
    logging.info('get_user_by_email() --> Sending data: ' + str(user))

    return make_response(jsonify({'user': user}))


@usr_api.route('/user/<user_id>', methods=['DELETE'])
def delete_user_by_id(user_id):
    try:
        bi = bson.objectid.ObjectId(user_id)
        User.objects.get(id=bi).delete()

    except ValidationError as e:
        logging.error(e.errors)

    return make_response('', 204)


@usr_api.route('/email/<email>', methods=['DELETE'])
def delete_user_by_email(email):
    try:
        User.objects.get(email=email).delete()

    except ValidationError as e:
        logging.error(e.errors)

    return make_response('', 204)
