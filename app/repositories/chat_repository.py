from app.models import db, Chat, Message

class ChatRepository:

    @staticmethod
    def get_chats_by_user(user_id: int):
        return Chat.query.filter(
            (Chat.user1_id == user_id) | (Chat.user2_id == user_id)
        ).order_by(Chat.last_updated.desc()).all()

    @staticmethod
    def get_chat_between_users(user1_id: int, user2_id: int):
        chat = Chat.query.filter(
            ((Chat.user1_id == user1_id) & (Chat.user2_id == user2_id)) |
            ((Chat.user1_id == user2_id) & (Chat.user2_id == user1_id))
        ).first()
        
        if chat is None:
            chat = Chat(user1_id= user1_id, user2_id= user2_id)
            ChatRepository.post_chat(chat= chat)
        return chat 
    
    @staticmethod
    def get_messages_by_chat(chat_id: int):
        return Message.query.filter_by(chat_id=chat_id).order_by(Message.timestamp.asc()).all()
    
    @staticmethod
    def post_messages_by_chat(sender_id: int, chat_id: int, content: int):

        message = Message(sender_id= sender_id, chat_id= chat_id, content= content)
        db.session.add(message)
        db.session.commit()
        return message

    @staticmethod
    def post_chat(chat: Chat):
        db.session.add(chat)
        db.session.commit()
        return chat

    
