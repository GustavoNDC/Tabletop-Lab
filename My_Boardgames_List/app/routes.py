from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session, flash
from app.models import Usuario, Jogos, Rank
from app import db
from sqlalchemy.orm import sessionmaker


def is_logged_in():
    return 'user_id' in session


# criação de um blueprint para rotas principais
main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/', methods=['POST', 'GET'])
def index():
    # criando as variaveis e recebendo os valores do GET
    query = Jogos.query
    filterQuery = query

    user = session['user']

    

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
    categList = filterQuery.with_entities(Jogos.categoria).all()
    categList = list(set(categList))
    for index in range(len(categList)):#limpando (' ',) da lista
        itemCategoria = str(categList[index])
        categList[index] = itemCategoria[2:-3:]
    
    # criando uma lista de donos unicos dos jogos
    donoList = filterQuery.with_entities(Jogos.dono).all()
    donoList = list(set(donoList))
    for index in range(len(donoList)):#limpando (' ',) da lista
        itemDono = str(donoList[index])
        donoList[index] = itemDono[2:-3:]

    # essas listas são usadas para criar todas as categorias no site
    # e receber o valor tambem

    rank = db.session.query(Rank).filter(Rank.id_user == user).all()
    print(rank)
    ranks_dict = {r.id_game: r.nota for r in rank}
    print(ranks_dict)
    for i in rank:
        print(i.id_game)
        print(i.nota)
    
    return render_template('index.html', jogos=jogos,
                           categList=categList,
                           donoList=donoList,
                           ranks=ranks_dict
                           )


    # Receber Valor da Nota do Usurario
@main_routes.route('/rate', methods=['GET', 'POST'])
def rate():
    if request.method == 'POST':
        id_user = request.form.get('user_id')
        id_game = request.form.get('jogo_id')
        nota = request.form.get('nota')
        print(f"Nota: {nota}, ID Usuário: {id_user}, ID Jogo: {id_game}") 

        nota_existente = Rank.query.filter_by(id_user=id_user, id_game=id_game).first()
        if nota_existente:
            nota_existente.nota = nota
            db.session.commit()

        else:
            nova_votacao = Rank(id_game=id_game, nota=nota, id_user=id_user)
            db.session.add(nova_votacao)
            db.session.commit()
        return redirect(url_for('main_routes.index'))

    return redirect(url_for('main_routes.index'))

        

@main_routes.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for('main_routes.perfil'))
    
    if request.method == 'POST':
        login = request.form.get('login')
        senha = request.form.get('senha')
        
        usuario_existente = Usuario.query.filter_by(login=login).first()


        
        if usuario_existente and usuario_existente.check_password(senha):


            session['user'] = usuario_existente.id
            flash('Login efetuado')
            return redirect(url_for('main_routes.perfil'))
            
        else:
            print('invalido')
            
            #new_user = Usuario(login=login)
            #new_user.set_password(senha)
            #db.session.add(new_user)
            #db.session.commit()

    return render_template('login.html')

@main_routes.route('/perfil', methods=['GET', 'POST'])
def perfil():
    if 'user' in session:
        user = session['user']
        return render_template('Perfil.html', user=user)

@main_routes.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('main_routes.login'))

