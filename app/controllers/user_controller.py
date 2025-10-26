from flask import Blueprint, request, jsonify
from ..services.user_service import UserService

bp = Blueprint('users', __name__)

@bp.route('', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return jsonify({'error': 'name, senha e email são obrigatórios para cadastro'}), 400
    try:
        user = UserService.create_user(name=name, email=email, password=password)
        return jsonify({'id': user.id, 'name': user.name, 'email':user.email}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password: 
        return jsonify({'error': 'email e senha sao obrigatórios para logar'}), 400
    try:
        user = UserService.login(email= email, password=password)
        return jsonify({'id': user.id, 'name': user.name, 'email':user.email}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


@bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserService.get_user(user_id)
    if not user:
        return jsonify({'error': 'Usuário não encontrado'}), 404
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email,'bairro': user.bairro})
