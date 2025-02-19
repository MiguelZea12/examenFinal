from app import db
from app.models.users import User
from app.schemas.users_schemas import user_schema, users_schema
from werkzeug.security import generate_password_hash

class UserService:
    @staticmethod
    def get_all_users():
        users = User.query.all()
        return users_schema.dump(users)

    @staticmethod
    def get_user_by_id(user_id):
        user = User.query.get(user_id)
        return user_schema.dump(user) if user else None

    @staticmethod
    def create_user(data):
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if User.query.filter_by(email=email).first():
            return {'message': 'Email already exists'}, 400
        
        new_user = User(
            username=username,
            email=email
        )
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        
        return user_schema.dump(new_user), 201

    @staticmethod
    def update_user(user_id, data):
        user = User.query.get(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        
        if 'password' in data:
            user.set_password(data['password'])
        
        db.session.commit()
        return user_schema.dump(user)

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        
        db.session.delete(user)
        db.session.commit()
        return {'message': 'User deleted successfully'}, 200