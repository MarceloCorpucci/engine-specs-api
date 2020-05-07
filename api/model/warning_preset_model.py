from flask_mongoengine import MongoEngine, ValidationError
from api.model.engine_model import Engine


db = MongoEngine()


MODES = ['Econo', 'Normal', 'Sport']


def preset_name(val):
    included = [False if not mode in val else True for mode in MODES]

    if not any(included):
        raise ValidationError('Preset name is not including the type')


class WarningPreset(db.Document):
    name = db.StringField(unique=True, validation=preset_name)
    ect_warning = db.IntField(required=True)
    oil_temp_warning = db.IntField(required=True)
    rpm_warning = db.IntField(required=True)
    engine = db.ReferenceField(Engine, required=True)
