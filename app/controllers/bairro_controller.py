from flask import Blueprint, request, jsonify
from ..services.bairro_service import BairroService

bp = Blueprint('bairros', __name__)

@bp.route('', methods=['POST'])
def create_bairro():
    data = request.get_json() or {}
    nome = data.get('nome')

    try:
        bairro = BairroService.create_bairro(nome)
        return jsonify({'id': bairro.id, 'nome': bairro.name}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@bp.route('', methods=['GET'])
def list_bairros():
    bairros = BairroService.list_bairros()
    return jsonify([{ 'id': b.id, 'nome': b.name } for b in bairros])

@bp.route('/<int:bairro_id>', methods=['GET'])
def get_bairro(bairro_id):
    bairro = BairroService.get_bairro(bairro_id)
    if not bairro:
        return jsonify({'error': 'Bairro não encontrado'}), 404
    return jsonify({'id': bairro.id, 'nome': bairro.name})