from flask_mongoengine import MongoEngine


db = MongoEngine()


class Engine(db.Document):
    model = db.StringField(unique=True)
    displacement = db.IntField(required=True)
    valve_amount = db.IntField()
    injectors = db.StringField()
    piston_type = db.StringField()
    camshaft = db.StringField()
    power = db.IntField(required=True)
    forced_induction = db.BooleanField(required=True)
    forced_induction_type = db.StringField()
    forced_induction_model = db.StringField()
    fuel_type = db.StringField()

