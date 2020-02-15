from flask_mongoengine import MongoEngine
from bson import ObjectId


db = MongoEngine()


class Engine(db.Document):
    id = ObjectId()
    model = db.StringField()
    displacement = db.IntField()
