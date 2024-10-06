from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Usuario {self.nome}>'

class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    rank = db.Column(db.Integer, unique=True)
    rankInHouse = db.Column(db.Integer, unique=True)
    nome = db.Column(db.String(80))
    nmJogadorMin = db.Column(db.Integer)
    nmJogadorMax = db.Column(db.Integer)
    categoria = db.Column(db.String(120))
    dificuldade = db.Column(db.Float)
    tempoDeJogo = db.Column(db.Integer)
    dono = db.Column(db.String(80))
    descricao = db.Column(db.String(120))