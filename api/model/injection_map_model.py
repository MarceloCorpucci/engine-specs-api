from flask_mongoengine import MongoEngine
from api.model.ecu_model import Ecu
from api.model.user_model import User


db = MongoEngine()


class InjectionMap(db.Document):
    map = db.ListField(required=True)
    date = db.DateTimeField(required=True)
    ecu = db.ReferenceField(Ecu, required=True)
    user = db.ReferenceField(User, required=True)
