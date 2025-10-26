from app.repositories.chat_repository import ChatRepository

class ChatService:

    @staticmethod
    def get_chats_for_user(user_id: int):
        chats = ChatRepository.get_chats_by_user(user_id)
        return [
            {
                "id": chat.id,
                "user1_id": chat.user1_id,
                "user2_id": chat.user2_id,
                "last_message": chat.last_message,
                "last_updated": str(chat.last_updated),
            }
            for chat in chats
        ]

    @staticmethod
    def get_chat_between(user1_id: int, user2_id: int):
        chat = ChatRepository.get_chat_between_users(user1_id, user2_id)
        if not chat:
            return None
        return {
            "id": chat.id,
            "user1_id": chat.user1_id,
            "user2_id": chat.user2_id,
            "last_message": chat.last_message,
            "last_updated": str(chat.last_updated),
        }

    @staticmethod
    def get_messages(chat_id: int):
        messages = ChatRepository.get_messages_by_chat(chat_id)
        return [
            {
                "id": msg.id,
                "chat_id": msg.chat_id,
                "sender_id": msg.sender_id,
                "content": msg.content,
                "timestamp": str(msg.timestamp),
            }
            for msg in messages
        ]
