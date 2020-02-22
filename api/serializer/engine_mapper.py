from kim import Mapper, field
from api.model.engine_model import Engine
from bson import ObjectId


class EngineMapper(Mapper):
        __type__ = Engine
        id = ObjectId()
        model = field.String()
        displacement = field.Integer()
        valve_amount = field.Integer()
        injectors = field.String(required=False)
        piston_type = field.String(required=False)
        camshaft = field.String(required=False)
        power = field.Integer()
        forced_induction = field.Boolean()
        forced_induction_type = field.String(required=False)
        forced_induction_model = field.String(required=False)
        fuel_type = field.String(required=False)


