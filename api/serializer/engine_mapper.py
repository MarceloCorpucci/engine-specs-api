from kim import Mapper, field
from api.model.engine_model import Engine
from bson import ObjectId


class EngineMapper(Mapper):
        __type__ = Engine()
        id = ObjectId()
        model = field.String()
        displacement = field.Integer()
