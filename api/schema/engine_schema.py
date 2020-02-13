from marshmallow_mongoengine import ModelSchema
from api.model.engine_model import Engine


# solution to error ModuleNotFoundError: No module named 'marshmallow.compat'
# https://github.com/touilleMan/marshmallow-mongoengine/issues/26


class EngineSchema(ModelSchema):
    class Meta:
        model = Engine

