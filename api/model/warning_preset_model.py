from flask_mongoengine import MongoEngine
from bson import ObjectId
from api.model.engine_model import Engine


db = MongoEngine()


class WarningPreset(db.Document):
    id = ObjectId()
    ect_warning = db.IntField()
    oil_temp_warning = db.IntField()
    rpm_warning = db.IntField()
    engine = db.ListField(db.EmbeddedDocumentField(Engine))
