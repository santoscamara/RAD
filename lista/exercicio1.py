#Leitura básica: Escreva um programa que leia um arquivo texto chamado poema.txt e exiba o
#número total de linhas e de palavras nele contidas


import os

caminho = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(caminho, "poema.txt")


try:
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

        total_linhas = len(linhas)
        total_palavras = 0

        for linha in linhas:
            palavras = linha.split()
            total_palavras += len(palavras)

    print(f"Número de linhas: {total_linhas}")
    print(f"Número de palavaras: {total_palavras}")

except FileNotFoundError:
    print("Erro: Não foi possível encontrar o arquivo 'poema.txt' ")
