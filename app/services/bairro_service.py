from ..models import Bairro
from ..repositories.bairro_repository import BairroRepository


class BairroService:
    @staticmethod
    def create_bairro(nome: str):
        if not nome:
            raise ValueError('Nome do bairro é obrigatório')
        existing = BairroRepository.get_by_nome(nome)
        if existing:
            raise ValueError('Bairro já cadastrado')
        bairro = Bairro(name= nome)
        return BairroRepository.add(bairro)


    @staticmethod
    def list_bairros():
        return BairroRepository.list_all()


    @staticmethod
    def get_bairro(bairro_id: int):
        return BairroRepository.get_by_id(bairro_id)