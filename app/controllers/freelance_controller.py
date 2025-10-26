from flask import Blueprint, request, jsonify
from ..services.freelance_service import FreelanceService

bp = Blueprint('freelances', __name__)

class Utils_FreelanceController:
    def get_freelance(freelance_id):
        freelance = FreelanceService.get_freelance(freelance_id)
        if not freelance:
            return jsonify({'error': 'Freelance não encontrado'}), 404
        return freelance


@bp.route('', methods=['POST'])
def create_freelance():
    data = request.get_json() or {}
    title = data.get('title')
    description = data.get('description')
    price = data.get('price')
    bairro_id = data.get('bairro')
    user_id = data.get('user_id')

    if not title or not bairro_id:
        return jsonify({'error': 'title e bairro são obrigatórios'}), 400
    try:
        freelance = FreelanceService.create_freelance(title=title,description=description, price=price or 0.0, bairro_id=bairro_id, user_id=user_id)
        return jsonify({
                'id': freelance.id, 
                'title': freelance.title,
                'bairro': freelance.bairro.name, 
                'price': freelance.price,
                'worker': freelance.worker.name 
                }), 201
    
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@bp.route('', methods=['GET'])
def list_freelances():
    bairro_id = request.args.get('bairro_id')
    user_id = request.args.get('user_id')

    freelances = FreelanceService.list_freelances(bairro_id= bairro_id, user_id= user_id)
    result = []
    for f in freelances:
        result.append({
        'id': f.id,
        'title': f.title,
        'description': f.description,
        'price': f.price,
        'bairro_id': f.bairro_id,
        'bairro': f.bairro.name,
        'user_id': f.user_id,
        'user_name': f.user.name,
        'worker_id': f.worker_id,
        'worker_name': f.worker_name
        })
    return jsonify(result)

@bp.route('/<int:freelance_id>', methods=['GET'])
def get_freelance(freelance_id):
    
    f = Utils_FreelanceController.get_freelance(freelance_id=freelance_id)

    return jsonify({
        'id': f.id,
        'title': f.title,
        'description': f.description,
        'price': f.price,
        'bairro_id': f.bairro_id,
        'bairro': f.bairro.name,
        'user_id': f.user_id,
        'user_name': f.user.name,
        'worker_id': f.worker_id,
        'worker_name': f.worker_name
    })


@bp.route('/<int:freelance_id>', methods=['PUT'])
def put_freelance_worker(freelance_id):
    data = request.args.get_json() or {}
    worker_id = data.get('worker_id')

    f = Utils_FreelanceController.get_freelance(freelance_id=freelance_id)

    try:
        f = FreelanceService.set_worker_freelances(freelance_id=freelance_id, worker_id=worker_id)
        if f:
            return jsonify({
            'id': f.id,
            'title': f.title,
            'description': f.description,
            'price': f.price,
            'bairro_id': f.bairro_id,
            'bairro': f.bairro.name,
            'user_id': f.user_id,
            'user_name': f.user.name,
            'worker_id': f.worker_id,
            'worker_name': f.worker_name
            })
    except ValueError as e:
        return jsonify({'error': str(e)}), 400



