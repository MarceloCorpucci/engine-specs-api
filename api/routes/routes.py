from flask import Blueprint, request, jsonify, make_response
import bson
from api.model.engine_model import Engine
from api.schema.engine_schema import EngineSchema  # engine_schema, engines_schema
from flasgger import swag_from


bp_api = Blueprint('api', __name__, url_prefix='/api')


@bp_api.route('/engines', methods=['GET'])
@swag_from('engines.yml')
def engines():
    get_engines = Engine.objects.all()
    schema = EngineSchema(many=True, only=['model', 'displacement'])
    all_engines = schema.dump(get_engines)

    return make_response(jsonify({'engines': all_engines}))


@bp_api.route('/engine/<id>', methods=['GET'])
def engine_detail(id):
    # bi = bson.objectid.ObjectId(id)
    get_engine = Engine.objects.get(id=id)
    schema = EngineSchema
    engine = schema.dump(get_engine)

    return make_response(jsonify({'engine': engine}))


@bp_api.route('/engine', methods=['POST'])
def create_engine():
    data = request.get_json()
    engine_to_save = Engine(model=data['model'], displacement=data['displacement'])
    engine_to_save.save()
    schema = EngineSchema
    saved_engine = schema.dump(engine_to_save)

    return make_response(jsonify({'engine': saved_engine}), 201)


@bp_api.route('/engine/<id>', methods=['DELETE'])
def delete_engine(id):
    # bi = bson.objectid.ObjectId(id)
    Engine.objects.get(id=id).delete()

    return make_response('', 204)
