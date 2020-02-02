from api.app import db


class Engine(db.Document):
    model = db.StringField()
    displacement = db.IntField()

