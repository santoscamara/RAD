#Escrita reversa: Crie um script que leia um arquivo dados.txt e salve seu conteúdo em um
#novo arquivo dados_reverso.txt , com as linhas na ordem inversa

import os

caminho = os.path.dirname(os.path.abspath(__file__))
caminho_entrada = os.path.join(caminho, 'dados.txt')
caminho_saida = os.path.join(caminho, 'dados_reversos.txt')

try:
    with open(caminho_entrada, 'r') as arquivo_origem:
        linhas = arquivo_origem.readlines()
        linhas_invertidas = linhas[::-1]

    with open(caminho_saida, "w") as arquivo_saida:
            arquivo_saida.writelines(linhas_invertidas)

except FileNotFoundError:
     print("Erro: Não foi possível encontrar o arquivo 'dados.txt")