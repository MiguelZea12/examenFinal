from flask_jwt_extended import create_access_token, decode_token
from app.models.users import User
from datetime import timedelta

class AuthService:
    @staticmethod
    def authenticate_user(email, password):
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            access_token = create_access_token(identity=user.id, expires_delta=timedelta(hours=1))
            return {'access_token': access_token, 'user': {'id': user.id, 'username': user.username, 'email': user.email}}, 200
        return {'message': 'Invalid email or password'}, 401

    @staticmethod
    def decode_access_token(token):
        try:
            decoded_token = decode_token(token)
            return decoded_token
        except Exception as e:
            return {'message': 'Invalid token', 'error': str(e)}, 401