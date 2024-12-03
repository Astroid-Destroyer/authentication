from flask import Flask, request, jsonify
from auth.controller import AuthController
from env import PORT


app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        return jsonify({'status': 'ok'}), 200
    

@app.route('/signup', methods=['POST'])   
def signup():
    if request.method == 'POST':
        try:
            data = request.json
        
            if 'email' not in data or 'password' not in data:
                return jsonify({"message": "missing credentials"}), 400
        
            email = data['email']
            password = data['password']

            auth_controller = AuthController()

            return auth_controller.signup(email=email, password=password);
        except Exception as e:
            print('[signup] Error:', e)
            return 'internal server error', 500
        

if __name__ == '__main__':
    app.run(port=PORT, debug=True)
