from flask_mongoengine import MongoEngine


db = MongoEngine()


class Engine(db.Document):
    model = db.StringField(unique=True)
    displacement = db.IntField()
    valve_amount = db.IntField()
    injectors = db.StringField(required=False)
    piston_type = db.StringField(required=False)
    camshaft = db.StringField(required=False)
    power = db.IntField()
    forced_induction = db.BooleanField()
    forced_induction_type = db.StringField(required=False)
    forced_induction_model = db.StringField(required=False)
    fuel_type = db.StringField(required=False)

