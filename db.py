from pymongo import MongoClient

from env import MONGODB_URI;

client = MongoClient(MONGODB_URI)
db = client['boishakh']