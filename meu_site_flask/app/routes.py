import requests
from flask import Blueprint, render_template, request, jsonify
from app.models import Usuario, Jogos
from app import db



# criação de um blueprint para rotas principais
main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/', methods=['GET', 'POST'])
def index():
    # criando as variaveis e recebendo os valores do POST
    query = Jogos.query
    jogadores = request.form.get('jogadores', 0)
    categoria = request.form.get('categoria', None)
    tempo = int(request.form.get('tempo', 9999))
    dono = request.form.get('dono', None)
    # "LIMPANDO" os valores do filtro
    if dono == 'null':
        dono = None

    if categoria == 'null':
        categoria = None
    
    # lidando em caso de erro na transformação de tempo e de jogadores
    try:
        jogadores = int(jogadores)
    except ValueError:
        jogadores = 0

    try:
        tempo = int(tempo)
    except ValueError:
        tempo = 9999

    # checando se houve algum input no filtro e o aplicando
    if jogadores > 0:
        query = query.filter(
            Jogos.nmJogadorMin <= jogadores,
            Jogos.nmJogadorMax >= jogadores
            )

    if dono != None:
        query = query.filter(
            Jogos.dono == dono
        )
    if categoria != None:
        query = query.filter(
            Jogos.categoria == categoria
        )
    
    jogos = query.all()
    
    # criando uma lista de categorias unicas dos jogos
    categList = query.with_entities(Jogos.categoria).all()
    categList = list(set(categList))
    for index in range(len(categList)):#limpando (' ',) da lista
        itemCategoria = str(categList[index])
        categList[index] = itemCategoria[2:-3:]
    
    # criando uma lista de donos unicos dos jogos
    donoList = query.with_entities(Jogos.dono).all()
    donoList = list(set(donoList))
    for index in range(len(donoList)):#limpando (' ',) da lista
        itemDono = str(donoList[index])
        donoList[index] = itemDono[2:-3:]

    # essas listas são usadas para criar todas as categorias no site
    # e receber o valor tambem


    
    return render_template('index.html', jogos=jogos,
                           categList=categList,
                           donoList=donoList
                           )
'''
@main_routes.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        novo_usuario = Usuario(nome=nome, email=email)
        db.session.add(novo_usuario)
        db.session.commit()
        return f"Obrigado pelo contato, {nome}!"
    return render_template('contato.html')

'''
