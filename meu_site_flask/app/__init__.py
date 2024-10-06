from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicializa a extensão do SQLAlchemy
db = SQLAlchemy()

def create_app():
    # Inicializa o Flask
    app = Flask(__name__)

    # Carrega as configurações do app
    app.config.from_pyfile('../config.py')

    # Inicializa a base de dados com o app
    db.init_app(app)

    # Importa e registra as rotas
    from app.routes import main_routes
    app.register_blueprint(main_routes)

    return app
