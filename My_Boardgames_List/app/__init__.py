from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicializa a extensão do SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Carrega as configurações do app
    app.config.from_pyfile('../config.py')

    # Inicializa a base de dados com o app
    db.init_app(app)

    # Importa e registra as rotas
    from app.routes.main_routes import main_routes
    from app.routes.graph_routes import graph_routes
    app.register_blueprint(main_routes)
    app.register_blueprint(graph_routes)

    return app
