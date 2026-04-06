import os

def obter_caminho_absoluto(nome_arquivo:str) -> None:
    """Retorna o caminho absoluto do arquivo com base na localização deste script"""
    diretorio_base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(diretorio_base, nome_arquivo)

def escrever_arquivo(caminho:str, conteudo: str, modo:list, cod:list) -> None:
    """Cria ou sobrescreve um arquivo com o conteúdo fornecido (Modo 'w')"""
    try:
        with open(caminho, modo, encoding = cod) as arquivo:
            arquivo.write(conteudo)
        print(f'[Sucesso] Arquivo escrito em: {caminho}')
    except Exception as e:
        print(f'[Erro] Falha ao escrever no arquivo: {e}')

def adicionar_texto(caminho:str, conteudo_add:str, modo:list,cod:list)-> None:
    """Adiciona conteúdo ao final de um arquivo existente (Modo 'a')"""
    try:
        with open(caminho, modo, encoding = cod) as arquivo:
            arquivo.write(conteudo_add)
            print(f'[Sucesso] Texto adicionado ao arquivo')
    except Exception as e:
        print(f'[Erro] Falha ao adicionar texto {e}')

def ler_arquivo(caminho:str, modo:list, cod:list) -> None:
    """Lê e retorna todo o conteúdo de um arquivo (Modo 'r')"""
    try:
        with open(caminho, modo, encoding = cod) as arquivo: 
            leitura = arquivo.read()
            print('\n--- Conteúdo do Arquivo ---')
            print(leitura)
            print('-------------------------------\n')
            return leitura
    except FileNotFoundError:
        print(f'[Erro] O arquivo não foi encontrado para leitura: {caminho}')
    except Exception as e:
        print(f'[Erro] falha ao ler o arquivo: {e}')

def apagar_arquivo(caminho: str) -> None:
    """Remove o arquivo do sistema operacional"""
    try:
        if os.path.exists(caminho):
            os.remove(caminho)
            print(f'[Sucesso] Arquivo Apagado: {caminho}')
        else:
            print(f'[Aviso] O arquivo {caminho} não existe para ser apagado')
    except Exception as e:
        print(f'[Erro] Falha ao apagar o arquivo {e}')


if __name__ == "__main__":
    modo = ['w', 'r', 'a']
    cod = ['utf-8', 'utf-32']
    count = 1
    while count <= 5:
        opcao = int(input("Opções:\n1 - Obter Caminho\n2 - Escrever Arquivo\n3 - Adicionar Texto\n4 - Ler Texto\n5 - Remover Texto\n"))
        match opcao:
            case 1:
                nome_arquivo = input("Digite o nome do arquivo: ")
                caminho = obter_caminho_absoluto(nome_arquivo)
            case 2:
                conteudo = input("O que deseja escrever no arquivo? ")
                escrever_arquivo(caminho, conteudo, modo[0],cod[0])
            case 3:
                conteudo_add = input("O que deseja acrescentar ao arquivo? ")
                adicionar_texto(caminho,  conteudo_add, modo[2], cod[0])
            case 4:
                print("Lendo o arquivo...\n")
                ler_arquivo(caminho, modo[1], cod[0])
            case 5:
                print('Apagando o arquivo...')
                apagar_arquivo(caminho)
            case _:
                print("Digite um número entre 1 e 5")
        count += 1