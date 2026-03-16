def abrir(caminho: str, modo: str) -> str:
    with open(caminho, modo) as arquivo:
        arquivo.write("\nPrimeira Linha")
        arquivo.write("\nSegunda Linha")
    return arquivo

def abrir_novamente(caminho: str, modo: str, linhas:list) -> str:
    with open(caminho, modo) as arquivo:
        arquivo.writelines(linhas)


if __name__ == "__main__":
    caminho = 'C:/Users/iagos/Documents/RAD/aula03/nomes.txt'
    caminho2 = 'C:/Users/iagos/Documents/RAD/aula03/nomes.txt'
    modo = 'w'
    linhas = ['Esta é a primeira linha', 'Esta é a segunda linha']
    abrir(caminho, modo)
    abrir_novamente(caminho, modo, linhas)
    

