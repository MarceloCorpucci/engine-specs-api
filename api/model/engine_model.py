from flask_mongoengine import MongoEngine
from bson import ObjectId


db = MongoEngine()


class Engine(db.Document):
    id = ObjectId()
    model = db.StringField()
    displacement = db.IntField()
    valve_amount = db.IntField()
    injectors = db.StringField()
    piston_type = db.StringField()
    camshaft = db.StringField()
    power = db.IntField()
    forced_induction = db.BooleanField()
    forced_induction_type = db.StringField()
    forced_induction_model = db.StringField()
    fuel_type = db.StringField()

