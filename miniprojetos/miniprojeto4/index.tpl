<!DOCTYPE html>
<html>
<head>
    <title>Jogo da Velha</title>
</head>
<body>
    <h1>Jogo da Velha</h1>
    <table border="1">
        % for linha in range(3):
        <tr>
            % for coluna in range(3):
            <td><a href="/jogar/{{linha}}/{{coluna}}">{{tabuleiro[linha][coluna]}}</a></td>
            % end
        </tr>
        % end
    </table>
    <p>Próximo jogador: {{'O' if jogador_atual == 'X' else 'X'}}</p>
    <p><a href="/reiniciar">Reiniciar Jogo</a></p>
</body>
</html>
