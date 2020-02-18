from flask import Blueprint, request, jsonify, make_response
import bson
from api.model.engine_model import Engine
from api.model.warning_preset_model import WarningPreset
from api.serializer.engine_mapper import EngineMapper
from api.serializer.warning_preset_mapper import WarningPresetMapper
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
    engine_to_save = Engine(model=data['model'],
                            displacement=data['displacement'],
                            power=data['power'],
                            forced_induction=data['forced_induction']
                            )
    engine_to_save.save()
    mapper = EngineMapper(obj=engine_to_save).serialize()

    return make_response(jsonify({'engine': mapper}), 201)


@bp_api.route('/engine/<id>', methods=['DELETE'])
def delete_engine(id):
    bi = bson.objectid.ObjectId(id)
    Engine.objects.get(id=bi).delete()

    return make_response('', 204)


@bp_api.route('/warning_preset', methods=['POST'])
def create_warning_preset():
    data = request.get_json()
    warn_preset_to_save = WarningPreset(ect_warning=data['ect_warning'],
                                        oil_temp_warning=data['oil_temp_warning'],
                                        rpm_warning=data['rpm_warning'],
                                        engine=data['engine']
                                        )
    warn_preset_to_save.save()
    mapper = WarningPresetMapper(obj=warn_preset_to_save).serialize()

    return make_response(jsonify({'warning_preset': mapper}), 201)
