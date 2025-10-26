from ..models import Bairro
from ..extensions import db


class BairroRepository:
    @staticmethod
    def add(bairro: Bairro):
        db.session.add(bairro)
        db.session.commit()
        return bairro

    @staticmethod
    def list_all():
        return Bairro.query.all()

    @staticmethod
    def get_by_id(bairro_id: int):
        return Bairro.query.get(bairro_id)

    @staticmethod
    def get_by_nome(nome: str):
        return Bairro.query.filter_by(name=nome).first()
    
