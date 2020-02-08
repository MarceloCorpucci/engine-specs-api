from flask import Blueprint, request, jsonify, make_response
import bson
from api.model.engine_model import Engine
from api.schema.engine_schema import engine_schema, engines_schema
from flasgger import swag_from


bp_api = Blueprint('api', __name__)


@bp_api.route('/api/engines', methods=['GET'])
@swag_from('engines.yml')
def engines():
    get_engines = Engine.objects.all()
    schema = engines_schema
    all_engines = schema.dump(get_engines)

    return make_response(jsonify({'engines': all_engines}))


@bp_api.route('/api/engine/<reg_id>', methods=['GET'])
def engine_detail(reg_id):
    bi = bson.objectid.ObjectId(reg_id)
    get_engine = Engine.objects.get(id=bi)
    schema = engine_schema
    engine = schema.dump(get_engine)

    return make_response(jsonify({'engine': engine}))


@bp_api.route('/api/engine', methods=['POST'])
def create_engine():
    data = request.get_json()
    engine_to_save = Engine(model=data['model'], displacement=data['displacement'])
    engine_to_save.save()
    schema = engine_schema
    saved_engine = schema.dump(engine_to_save)

    return make_response(jsonify({'engine': saved_engine}), 201)


@bp_api.route('/api/engine/<id>', methods=['DELETE'])
def delete_engine(id):
    bi = bson.objectid.ObjectId(id)
    Engine.objects.get(id=bi).delete()

    return make_response('', 204)
