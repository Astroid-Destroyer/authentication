from flask import jsonify
from auth.service import AuthService


class AuthController:
    def __init__(self):
        self.__service = AuthService()

    def signup(self, email, password):
        try:
            if self.__service.signup(email=email, password=password):
                return jsonify({'message': 'User created successfully'}), 201
            else:
                return jsonify({'message': 'User already exists'}), 409
        except Exception as e:
            print('[auth.signup] Error:', e)
            return 'Failed to create user', 500