# Import necessário
import matplotlib.pyplot as plt
import io
import base64
from flask import Blueprint, render_template, Response
from app.models import Usuario, Jogos, Notas
from app.utils.ranking_helpers import calcular_ranking, botão_da_loucura

graph_routes = Blueprint('graph_routes', __name__)

@graph_routes.route('/graficos')
def cluster_user_avaliacao():
    # Dados de exemplo
    x = [1, 2, 3, 4]
    y = [10, 20, 25, 30]

    #Segmentação de Usuários com Clustering:
    #Pergunta: Podemos agrupar os usuários com base em seus padrões de avaliação?

    #Objetivo: Identificar diferentes tipos de jogadores, como aqueles que preferem jogos mais complexos ou aqueles que sempre dão notas altas.
    
    #Análise: Você pode aplicar técnicas de clustering (como K-means ou DBSCAN) para segmentar os usuários com base nas avaliações que eles deram. Isso pode gerar insights sobre perfis de jogadores.

    # Criando o gráfico de linha
    plt.figure()
    plt.scatter(x, y)
    plt.title("Exemplo de Gráfico de Linha")
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")

    # Salvando o gráfico em um buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    # Convertendo o gráfico em uma string base64
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()

    # Passando a string para o template
    return render_template('graficos.html', grafico=image_base64)
