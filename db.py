import os, bcrypt
from pymongo import MongoClient

client = MongoClient(os.getenv('MONGODB_URI'))
db = client['My-berry']
# collection = db['']
def encrypt_password(password):
    salt = bcrypt.gensalt(10)
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
def create_user(email,password):
    users = db['users']
    check_email = users.find_one({'email':email})
    if check_email:
        return 409
    users.insert_one({'email':email,'password':encrypt_password(password)})
    return 201
    
    



