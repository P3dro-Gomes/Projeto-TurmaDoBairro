from ..models import Freelance, User
from ..repositories.freelance_repository import FreelanceRepository
from ..repositories.user_repository import UserRepository

class FreelanceService:
    
    @staticmethod
    def create_freelance(title: str, description: str, price: float, bairro_id: int, user_id: int = None):
        if not bairro_id:
            raise ValueError('bairro_id é obrigatório')

        user = None
        if user_id is not None:
            user = UserRepository.get_by_id(user_id)
            if not user:
                raise ValueError('Usuário informado não existe')

        freelance = Freelance(title=title, description=description, price=price, bairro_id=bairro_id, user=user)
        return FreelanceRepository.add(freelance)

    @staticmethod
    def get_freelance(freelance_id: int):
        return FreelanceRepository.get_by_id(freelance_id)
    
    @staticmethod
    def list_freelances(bairro_id: int = None, user_id: int = None):
        if bairro_id:
            return FreelanceRepository.find_by_bairroID(bairro_id)
        if user_id: 
            return FreelanceRepository.find_by_userID(user_id=user_id) 
        
        return FreelanceRepository.list_all()
    
    @staticmethod
    def set_worker_freelances(freelance_id: int, worker_id: int):
            
        freelance = FreelanceRepository.get_by_id(freelance_id)      
        if not freelance:
            raise ValueError('Freelance informado não existe')
        
        worker_id = UserRepository.get_by_id(worker_id)
        if not worker_id:
            raise ValueError('Usuário informado não existe')
        
        return FreelanceRepository.set_worker(freelance_id=freelance_id, worker_id=worker_id)
