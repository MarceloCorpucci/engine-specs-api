from flask_mongoengine import MongoEngine


db = MongoEngine()


class Engine(db.Document):
    # id = db.BinaryField(primary_key=True)
    model = db.StringField()
    displacement = db.IntField()

