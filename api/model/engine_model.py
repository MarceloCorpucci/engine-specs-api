from flask_mongoengine import MongoEngine


db = MongoEngine()


class Engine(db.Document):
    model = db.StringField()
    displacement = db.IntField()

