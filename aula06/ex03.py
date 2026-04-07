import os

def criar_diretorio(nome_diretorio:str)->None:
    try:
        os.makedirs(nome_diretorio)
        print(f"O diretorio '{nome_diretorio}' foi criado com sucesso.")
    except FileExistsError:
        print(f"O diretório '{nome_diretorio} já existe.")
    except PermissionError:
        print(f"Permissão negada para criar o diretório '{nome_diretorio}'.")
    except Exception as e:
        print(f"Ocorreu um erro ao criar o diretório '{nome_diretorio}': {e}")

def criar_arquivo(arquivo_nome: str, conteudo:str)->None:
    try:
        with open(arquivo_nome, 'w') as file:
            file.write(conteudo)
        print(f"O arquivo '{arquivo_nome}' foi criado com sucesso.")
    except PermissionError:
        print(f"Permissão negada parar criar o arquivo '{arquivo_nome}'.")
    except Exception as e:
        print(f"Ocorreu um erro ao criar o arquivo '{arquivo_nome}': {e}")
        
