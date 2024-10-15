import os

# Caminho absoluto para o arquivo do banco de dados
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Configurações da aplicação
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'instance', 'meu_banco.db')
SQLALCHEMY_ENGINE_OPTIONS =  {"connect_args": {"timeout": 10}, 'connect_args': {'check_same_thread': False}}
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'adm12345'
