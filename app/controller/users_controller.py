from flask import Blueprint, request, jsonify
from app.service.users_service import UserService

users_bp = Blueprint('users_bp', __name__)

@users_bp.route('/', methods=['GET'])
def get_users():
    return jsonify(UserService.get_all_users())

@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserService.get_user_by_id(user_id)
    if user:
        return jsonify(user)
    return jsonify({'message': 'User not found'}), 404

@users_bp.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    return UserService.create_user(data)

@users_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    return UserService.update_user(user_id, data)

@users_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return UserService.delete_user(user_id)