from ..models import User
from ..extensions import db

class UserRepository:
    @staticmethod
    def add(user: User):
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def login(email: str, password: str):
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            return user
        else:
            return None

    @staticmethod
    def get_by_id(user_id: int):
        return User.query.get(user_id)

    @staticmethod
    def get_by_email(email: str):
        return User.query.filter_by(email=email).first()
    
    @staticmethod
    def list_all():
      return User.query.all()
    
    