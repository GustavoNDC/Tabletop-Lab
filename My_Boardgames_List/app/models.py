from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(120), nullable=False)
    
    # Define a senha, gerando o hash e atribuindo ao campo senha
    def set_password(self, senha):
        self.senha = generate_password_hash(senha)

    def check_password(self, senha):
        return check_password_hash(self.senha, senha)

    def __repr__(self):
        return f'<Usuario {self.login}>'

class Jogos(db.Model):
    __tablename__ = 'jogos'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    rank = db.Column(db.Integer, unique=True)
    rankInHouse = db.Column(db.Integer)
    nome = db.Column(db.String(80))
    nmJogadorMin = db.Column(db.Integer)
    nmJogadorMax = db.Column(db.Integer)
    categoria = db.Column(db.String(120))
    dificuldade = db.Column(db.Float)
    tempoDeJogo = db.Column(db.Integer)
    dono = db.Column(db.String(80))
    descricao = db.Column(db.String(120))
    img = db.Column(db.String(999))
    def __repr__(self):
        return f'<Jogos {self.nome}>'

class Notas(db.Model):
    __tablename__ = 'notas'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    id_user = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    id_game = db.Column(db.Integer, db.ForeignKey('jogos.id'), nullable=False)
    nota = db.Column(db.Integer)
    def __repr__(self):
        return f"<Notas(id='{self.id}', id_user='{self.id_user}', id_game='{self.id_game}', nota='{self.nota}')>"

class Generos(db.Model):
    __tablename__ = 'generos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)

class JogoGenero(db.Model):
    __tablename__ = 'jogos_generos'
    id_jogo = db.Column(db.Integer, db.ForeignKey('jogos.id'), primary_key=True)
    id_genero = db.Column(db.Integer, db.ForeignKey('generos.id'), primary_key=True)

class Ranking(db.Model):
    __tablename__='ranking'
    id_jogo = db.Column(db.Integer, primary_key=True)
    media_nota = db.Column(db.Numeric(3, 2))
    def __repr__(self):
        return f"<Ranking id_jogo={self.id_jogo} media_nota={self.media_nota}>"


