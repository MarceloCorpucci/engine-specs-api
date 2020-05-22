from flask_mongoengine import MongoEngine
from passlib.hash import pbkdf2_sha256 as sha256


db = MongoEngine()


class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, max_length=255)
    active = db.BooleanField(default=True)

    def add_user(self):
        self.collection.insert({
            'email': self.email,
            'password': sha256.hash(self.password),
            'active': self.active
        })

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, a_hash):
        return sha256.verify(password, a_hash)

    @classmethod
    def find_by_email(cls, email):
        return cls.objects.get(email=email)
