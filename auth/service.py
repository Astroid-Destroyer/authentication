import bcrypt
from db import db

class AuthService:
    def __init__(self, collection='auth'):
        self.__collection = db[collection]

    def __encrypt(self, password):
        salt = bcrypt.gensalt(10)
        return bcrypt.hashpw(password.encode('utf-8'), salt)

    def signup(self, email, password):
        user = self.__collection.find_one({ 'email': email })
        if not user:
            self.__collection.insert_one({
                'email': email,
                'password': self.__encrypt(password)
            })
            return True
        return False

