from flask_mongoengine import MongoEngine
from api.model.engine_model import Engine


db = MongoEngine()


class WarningPreset(db.Document):
    ect_warning = db.IntField(required=True)
    oil_temp_warning = db.IntField(required=True)
    rpm_warning = db.IntField(required=True)
    engine = db.ReferenceField(Engine, required=True)
