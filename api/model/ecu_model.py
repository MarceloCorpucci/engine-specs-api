from flask_mongoengine import MongoEngine
from api.model.engine_model import Engine
from api.model.warning_preset_model import WarningPreset
from api.model.user_model import User


db = MongoEngine()


class Ecu(db.Document):
    model = db.StringField(unique=True)
    firmware = db.Stringield(required=True)
    date_added = db.DateTimeField(required=True)
    engine = db.ReferenceField(Engine, required=True)
    warning_preset = db.ReferenceField(WarningPreset, required=True)
    user = db.ReferenceField(User, required=True)

