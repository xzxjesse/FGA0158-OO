from bottle import Bottle, run, template, request

app = Bottle()

# Estrutura de dados para o tabuleiro do jogo
tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
jogador_atual = 'X'

# Rota para a página inicial
@app.route('/')
def index():
    return template('index', tabuleiro=tabuleiro)

# Rota para processar as jogadas
@app.route('/jogar/<linha:int>/<coluna:int>')
def jogar(linha, coluna):
    global jogador_atual
    if tabuleiro[linha][coluna] == ' ':
        tabuleiro[linha][coluna] = jogador_atual
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

    return index()

# Função para reiniciar o jogo
@app.route('/reiniciar')
def reiniciar():
    global tabuleiro, jogador_atual
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogador_atual = 'X'
    return index()

# Executa o aplicativo Bottle
if __name__ == '__main__':
    run(app, host='localhost', port=8080)
