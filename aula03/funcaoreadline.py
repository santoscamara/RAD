def linhas(caminho_arquivo: str, modo: str) -> list:
    arquivo = open(caminho_arquivo, modo)
    linhas = arquivo.readlines()
    arquivo.close()
    return linhas

if __name__ == "__main__":
    caminho_arquivo = 'C:/Users/iagos/Documents/RAD/aula03/nomes.txt'
    m = 'r'
    l = linhas(caminho_arquivo, m)
    for i, linha in enumerate(l, start = 1):
        print(f'Linha {i} - {linha}')