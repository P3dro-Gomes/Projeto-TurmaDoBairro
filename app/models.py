from .extensions import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class Bairro(db.Model):
    __tablename__ = 'bairros'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    freelances = db.relationship('Freelance', back_populates='bairro')

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200),nullable= False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    freelances = db.relationship('Freelance', back_populates='user', foreign_keys='Freelance.user_id')
    assigned_freelances = db.relationship('Freelance', back_populates='worker', foreign_keys='Freelance.worker_id')


    chats_as_user1 = db.relationship('Chat', foreign_keys='Chat.user1_id', back_populates='user1')
    chats_as_user2 = db.relationship('Chat', foreign_keys='Chat.user2_id', back_populates='user2')
    messages_sent = db.relationship('Message', back_populates='sender')


    def set_password(self, password):
        self.password = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password, password)


class Freelance(db.Model):
    __tablename__ = 'freelances'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    bairro_id = db.Column(db.Integer, db.ForeignKey('bairros.id'))
    worker_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable= True)

    user = db.relationship('User', back_populates='freelances', foreign_keys=[user_id])
    bairro = db.relationship('Bairro', back_populates='freelances')
    worker = db.relationship('User', back_populates='assigned_freelances', foreign_keys=[worker_id])


class Chat(db.Model):
    __tablename__ = 'chat'

    id = db.Column(db.Integer, primary_key=True)

    user1_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user2_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    last_message = db.Column(db.Text)
    last_updated = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    __table_args__ = (
        db.UniqueConstraint('user1_id', 'user2_id', name='unique_chat_pair'),
    )

    user1 = db.relationship('User', foreign_keys=[user1_id], back_populates='chats_as_user1')
    user2 = db.relationship('User', foreign_keys=[user2_id], back_populates='chats_as_user2')
    messages = db.relationship('Message', back_populates='chat', cascade='all, delete-orphan')

    created_at = db.Column(db.DateTime, default=db.func.now())


class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)

    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'), nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.now())

    chat = db.relationship('Chat', back_populates='messages')
    sender = db.relationship('User', back_populates='messages_sent')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if self.chat:
            self.chat.last_message = self.content
            self.chat.last_updated = db.func.now()

    def __repr__(self):
        return f"<Message {self.id} from {self.sender_id} in chat {self.chat_id}>"
