from flask import Blueprint, request
from api.model.user_model import User
from flask_jwt_extended import create_access_token
from api.utils.responses import response_with
from api.utils import responses as resp
import logging


logging.basicConfig(level=logging.INFO)


usr_api = Blueprint('user_routes', __name__, url_prefix='/api/users')


@usr_api.route('/user', methods=['POST'])
def create_user():
    try:
        request_data = request.get_json()
        request_data['password'] = User.generate_hash(request_data['password'])

        user = User(email=request_data['email'], password=request_data['password'])
        user.save()

        return response_with(resp.SUCCESS_201)

    except Exception as e:
        logging.error(e)
        return response_with(resp.INVALID_INPUT_422)


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
