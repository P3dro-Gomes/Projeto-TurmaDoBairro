from app.models import db, Chat, Message

class ChatRepository:

    @staticmethod
    def get_chats_by_user(user_id: int):
        return Chat.query.filter(
            (Chat.user1_id == user_id) | (Chat.user2_id == user_id)
        ).order_by(Chat.last_updated.desc()).all()

    @staticmethod
    def get_chat_between_users(user1_id: int, user2_id: int):
        return Chat.query.filter(
            ((Chat.user1_id == user1_id) & (Chat.user2_id == user2_id)) |
            ((Chat.user1_id == user2_id) & (Chat.user2_id == user1_id))
        ).first()

    @staticmethod
    def get_messages_by_chat(chat_id: int):
        return Message.query.filter_by(chat_id=chat_id).order_by(Message.timestamp.asc()).all()
    


    
