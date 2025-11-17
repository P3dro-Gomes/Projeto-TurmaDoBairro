from flask import Blueprint, jsonify, request
from app.services.chat_service import ChatService

bp = Blueprint('chats', __name__)

@bp.route('', methods=['GET'])
def get_chats_by_user():
    user_id = request.args.get('user_id', type=int)
    if not user_id:
        return jsonify({"error": "user_id é obrigatório"}), 400

    chats = ChatService.get_chats_for_user(user_id)
    return jsonify(chats), 200


@bp.route('/existing', methods=['GET'])
def get_existing_chat():
    user1_id = request.args.get('user1_id', type=int)
    user2_id = request.args.get('user2_id', type=int)

    if not user1_id or not user2_id:
        return jsonify({"error": "user1_id e user2_id são obrigatórios"}), 400

    chat = ChatService.get_chat_between(user1_id, user2_id)
    if not chat:
        return jsonify({"exists": False}), 200

    return jsonify({"exists": True, "chat": chat}), 200


@bp.route('/messages', methods=['GET'])
def get_messages():
    chat_id = request.args.get('chat_id', type=int)
    if not chat_id:
        return jsonify({"error": "chat_id é obrigatório"}), 400

    messages = ChatService.get_messages(chat_id)
    return jsonify(messages), 200


@bp.route('/messages', methods=['POST'])
def post_messages():
    
    chat_id = request.args.get('chat_id', type=int)
    sender_id = request.args.get('sender_id', type=int)
    content = request.args.get('content', type=int)

    if not chat_id or sender_id or content:
        return jsonify({"error": "Faltando informaçoes"}), 400

    messages = ChatService.post_message(sender_id= sender_id, chat_id= chat_id, content= content)
    return jsonify(messages), 200
