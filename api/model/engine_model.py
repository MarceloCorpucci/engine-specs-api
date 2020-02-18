from flask_mongoengine import MongoEngine
from bson import ObjectId


db = MongoEngine()


class Engine(db.EmbeddedDocument):
    id = ObjectId()
    model = db.StringField()
    displacement = db.IntField()
    power = db.IntField()
    forced_induction = db.BooleanField()
