from flask import Flask
from .config import Config
from .extensions import db
from .controllers import user_controller, freelance_controller, bairro_controller,chat_controller

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(user_controller.bp, url_prefix='/users')
    app.register_blueprint(freelance_controller.bp, url_prefix='/freelances')
    app.register_blueprint(bairro_controller.bp, url_prefix='/bairros')
    app.register_blueprint(chat_controller.bp, url_prefix='/chats')

    @app.route('/')
    def index():
        return {'message': 'API Freelancer — com bairros integrados'}

    return app
