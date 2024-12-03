import os
from dotenv import load_dotenv

load_dotenv()

__mongodb_uri = os.getenv('MONGODB_URI')
__env_port = os.getenv('PORT')

if __mongodb_uri is None:
    raise ValueError("Please set the MONGODB_URI environment variable")

MONGODB_URI = __mongodb_uri
PORT = 8080 if __env_port is None else int(__env_port)