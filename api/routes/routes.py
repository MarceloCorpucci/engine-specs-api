from flask import Blueprint, request, jsonify, make_response
import bson
from api.model.engine_model import Engine
from api.serializer.engine_mapper import EngineMapper
from flasgger import swag_from


bp_api = Blueprint('api', __name__, url_prefix='/api')


@bp_api.route('/engines', methods=['GET'])
@swag_from('engines.yml')
def engines():
    engine = Engine.objects.all()
    mapper = EngineMapper.many(obj=engine).serialize(objs=engine)

    return make_response(jsonify({'engines': mapper}))


@bp_api.route('/engine/<id>', methods=['GET'])
def engine_detail(id):
    bi = bson.objectid.ObjectId(id)
    engine = Engine.objects.get(id=bi)
    mapper = EngineMapper(obj=engine).serialize()

    return make_response(jsonify({'engine': mapper}))


@bp_api.route('/engine', methods=['POST'])
def create_engine():
    data = request.get_json()
    engine_to_save = Engine(model=data['model'], displacement=data['displacement'])
    engine_to_save.save()
    mapper = EngineMapper(obj=engine_to_save).serialize()

    return make_response(jsonify({'engine': mapper}), 201)


@bp_api.route('/engine/<id>', methods=['DELETE'])
def delete_engine(id):
    bi = bson.objectid.ObjectId(id)
    Engine.objects.get(id=bi).delete()

    return make_response('', 204)
