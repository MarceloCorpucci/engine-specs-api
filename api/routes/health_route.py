from flask import Blueprint, make_response, jsonify
import logging


logging.basicConfig(level=logging.INFO)


health_check_api = Blueprint('health_check_api', __name__, url_prefix='/api')


@health_check_api.route('/health_check', methods=['GET'])
def get_health_check():
    logging.info('get_health_check() --> Retrieving request from client.')

    return make_response(jsonify({'status': 'OK'}), 200)
