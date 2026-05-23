from banco import BancoDeDados
from pessoa import Pessoa
from veiculo import Veiculo
from marca import Marca


if __name__ == "__main__":
#Criando uma instancia de BancoDeDados
    banco = BancoDeDados()
#Conectando ao banco de dados
    banco.conectar()
#Criando as tabelas necessárias
    banco.criar_tabelas()
#Inserindo uma pessoa
    pessoa1 = Pessoa(cpf=12345678900, nome="Joaquim", nascimento="1977-08-18", oculos=True)
    pessoa2 = Pessoa(cpf=13242352399, nome="Maria", nascimento="1985-05-01", oculos=False)
    pessoa3 = Pessoa(cpf=32378237123, nome="Carlos", nascimento="1992-10-05", oculos=True)
    banco.inserir_pessoa(pessoa1)
    banco.inserir_pessoa(pessoa2)
    banco.inserir_pessoa(pessoa3)
#Inserindo uma marca
    marca1 = Marca(id=1,nome="FIAT",sigla="FIA")
    marca2 = Marca(id=2, nome="VOLKSWAGEN", sigla ="VW")
    marca3 = Marca(id=3, nome="BUILD YOUR DREAMS", sigla="BYD")
    banco.inserir_marca(marca1)
    banco.inserir_marca(marca2)
    banco.inserir_marca(marca3)
#Inserindo um veiculo
    veiculo1 = Veiculo(placa="LRW1I27", cor="Cinza", proprietario=pessoa1, marca=marca1)
    veiculo2 = Veiculo(placa="XLO3H83", cor="Branco", proprietario=pessoa2, marca=marca2)
    veiculo3 = Veiculo(placa="MDR2K54", cor="Preto", proprietario=pessoa3, marca=marca3)
    banco.inserir_veiculo(veiculo1)
    banco.inserir_veiculo(veiculo2)
    banco.inserir_veiculo(veiculo3)
#Buscando  todas as pessoas
    print("Pessoas: ")
    for pessoa in banco.buscar_todas_pessoas():
        print(pessoa)

#Buscando todas as marcas:
    print("\nMarcas: ")
    for marca in banco.buscar_todas_marcas():
        print(marca)

#Buscando todos os veiculos
    print("\nVeiculos: ")
    for veiculo in banco.buscar_todos_veiculos():
        print(veiculo)


#Fechando a conexão
    banco.fechar_conexao()
