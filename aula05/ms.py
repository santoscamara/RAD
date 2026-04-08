## funcao-ms.py

import os
def manipulandoartexto(caminho:str, modo: list, texto: str)-> None:
    with open(caminho, modo, encoding = 'utf-8') as arquivo:
        arquivo.write(texto)

if __name__ == "__main__":
    caminho = os.path.dirname(__file__)
    modo = ['w', 'r', 'a']
    texto = "Aula manipulando string."
    print(texto[0:24:2])
    manipulandoartexto(caminho, modo[0], texto)
