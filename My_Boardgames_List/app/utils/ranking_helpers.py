from app.models import Notas, Ranking, Jogos, Usuario
import random
from app import db

def calcular_ranking():
    index = 0
    rankings = db.session.query(
        Notas.id_game,
        db.func.avg(Notas.nota).label('media_nota')
    ).group_by(Notas.id_game).order_by(db.func.avg(Notas.nota).desc()).all()

    # Atualizando tabela de rankings
    for ranking in rankings:
        id_jogo = ranking.id_game
        media_nota = ranking.media_nota
        index += 1

        ranking_existente = db.session.query(Ranking).filter(Ranking.id_jogo == id_jogo).first()
        jogo_existente = db.session.query(Jogos).filter(Jogos.id == id_jogo).first()

        if ranking_existente:
            ranking_existente.media_nota = media_nota
            jogo_existente.rankInHouse = index
        else:
            novo_ranking = Ranking(id_jogo=id_jogo, media_nota=media_nota)
            db.session.add(novo_ranking)
            jogo_existente.rankInHouse = index

    db.session.commit()


# Essa função aleatoriza TODAS as notas do banco de dados de TODOS os usuarios
def botão_da_loucura():
    usuarios = Usuario.query.all()
    jogos = Jogos.query.all()
    
    for user in usuarios:
        for game in jogos:
            nota_aleatoria = random.randint(1, 10)
            nova_nota = Notas(id_user=user.id, id_game=game.id, nota=nota_aleatoria)

            nota_existente = Notas.query.filter_by(id_user=user.id, id_game=game.id).first()

            if nota_existente:
                nota_existente.nota = nota_aleatoria
            else:
                db.session.add(nova_nota)

    db.session.commit()
 
