from flask import Flask, request, jsonify
import bcrypt
from dotenv import load_dotenv  # Correct import
import os
from db import create_user
# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        return jsonify({'status': 'ok'}), 200
    else:
        return "NOT FOUND", 404
    
def encrypt_password(password):
    salt = bcrypt.gensalt(10)
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

@app.route('/signup', methods=['POST'])   
def signup():
    if request.method == 'POST':
        data = request.json
        
        if 'email' not in data or 'password' not in data:
            return jsonify({"message": "missing credentials"}), 400
        
        email = data['email']
        password = data['password']
        
        try:
            create_user(email,password)
        
        except Exception as e:
            return jsonify({"message": "error creating user"}), 500
        
        return jsonify({'message': 'User created successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
    print(os.getenv('sampriti'))  
