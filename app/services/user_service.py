from ..models import User
from ..repositories.user_repository import UserRepository

class UserService:
    @staticmethod
    def create_user(name: str, email: str, password: str):
        existing = UserRepository.get_by_email(email)

        if existing:
            raise ValueError('Usuário com esse email já existe')

        user = User(name=name, email=email)
        user.set_password(password=password)

        return UserRepository.add(user)
        
    @staticmethod
    def get_user(user_id: int):
        return UserRepository.get_by_id(user_id)
    
    @staticmethod
    def login(email: str, password: str):
        user = UserRepository.login(email=email, password=password)
        if not user:
            raise ValueError("Email ou senha incorretos")
        
        return user

    @staticmethod
    def list_users():
        return UserRepository.list_all()