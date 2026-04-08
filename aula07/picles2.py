import pickle

def cria_picles(nome: str, modo: list) -> None:
    try:
        with open(nome, modo) as salva_binario:
            pickle.dump(nome, salva_binario)
        print("Dados salvos com sucesso", )
    except pickle.PicklingError as e:
        print(f"Ocorreu um erro ao salvar os dados: {e}")

def le_picles(nome:str, modo:list) -> None:
    try:
        with open(nome, modo) as carrega_binario:
            dados_carregados = pickle.load(carrega_binario)
        print("Dados carregados com sucesso", dados_carregados)
    except pickle.UnpicklingError as e:
        print(f"Ocorreu um erro ao carregar os dados: {e}")

if __name__ == "__main__":
    modos = ["wb", "rb", "ab"]
    nome = "Iago"
    cria_picles(nome, modos[0])
    le_picles(nome, modos[1])
    


