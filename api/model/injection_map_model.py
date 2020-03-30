from flask_mongoengine import MongoEngine
from api.model.user_model import User


db = MongoEngine()


class InjectionMap(db.Document):
    map = db.ListField(required=True)
    date = db.DateTimeField(required=True)
    user = db.ReferenceField(User, required=True)
