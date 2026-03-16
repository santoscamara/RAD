#Manipulação de arquivos

def escrever_arquivo(caminho: str, modo: tuple) -> str:
    arquivo = open(caminho, modo)
    arquivo.write("Marcos")
    arquivo.writelines(["\nMarcela", "\nBeatriz", "\nCarola"])
    arquivo.close()
    return arquivo

def ler_arquivo(caminho: str, modo: tuple) -> str:
    arquivo = open(caminho, modo)
    linhas = arquivo.readlines()
    arquivo.close()
    return linhas

if __name__ == "__main__":
    caminho = 'C:/Users/iagos/Documents/RAD/aula03/nomes2.txt'
    modo = 'w', 'r'
    escrever_arquivo(caminho, modo[0])
    linhas = ler_arquivo(caminho, modo[1])
    for i, linha in enumerate(linhas, start = 1):
        print(f'Linha{i} - {linha}')
    


