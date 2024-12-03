from app import app
from waitress import serve
from env import PORT

if __name__ == "__main__":
    serve(app, port=PORT)