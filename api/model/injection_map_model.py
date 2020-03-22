from flask_mongoengine import MongoEngine
from api.model.user_model import User


db = MongoEngine()


class InjectionMap(db.Document):
    map = db.DictField(required=True)
    date = db.DateField(required=True)
    user = db.ReferenceField(User, required=True)
