from ..models import Freelance
from ..extensions import db

class FreelanceRepository:
    
    @staticmethod
    def add(freelance: Freelance):
        db.session.add(freelance)
        db.session.commit()
        return freelance
    
    @staticmethod
    def get_by_id(freelance_id: int):
        return Freelance.query.get(freelance_id)    
    
    @staticmethod
    def list_all():
        return Freelance.query.filter(Freelance.worker_id != None).order_by(Freelance.created_at.desc()).all()
     
    @staticmethod
    def find_by_bairroID(bairro_id: int):
        return Freelance.query.filter(Freelance.bairro_id == bairro_id).order_by(Freelance.created_at.desc()).all()

    @staticmethod
    def find_by_userID(user_id: int):
        return Freelance.query.filter(Freelance.user_id == user_id or Freelance.worker_id == user_id).order_by(Freelance.created_at.desc()).all()

    @staticmethod
    def set_worker(freelance_id: int, worker_id: int):
        freelance = FreelanceRepository.get_by_id(freelance_id)
        if not freelance:
            return None
        
        setattr(freelance, worker_id, worker_id)
        db.session.commit()
        return freelance


