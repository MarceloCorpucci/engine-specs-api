from flask_mongoengine import MongoEngine
from passlib.hash import pbkdf2_sha256 as sha256


db = MongoEngine()


class User(db.Document):
    email = db.EmailField(unique=True)
    password = db.StringField(unique=True)

    # def create(self, email, password):
    #     self.email = email
    # 	self.password = password

    @classmethod
    def find_by_email(cls, email):
        return cls.get(email=email)

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)
