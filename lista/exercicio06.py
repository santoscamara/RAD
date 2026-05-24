#Parser de JSON: Escreva um script que leia o arquivo produtos.json criado no exercício
#anterior e exiba o valor total em dinheiro do estoque disponível (preço estoque).
import json
import os

caminho = os.path.dirname(os.path.abspath(__file__))
arquivo_json = os.path.join(caminho, "produtos.json")


try:
    with open(arquivo_json, 'r', encoding='utf-8') as arquivo_origem:
        dados = json.load(arquivo_origem)

    valor_total = 0.0

    print(f"--- Resumo do Estoque por Produto ---")

    for produto in dados["produtos"]:
        nome = produto["nome"]
        preço = produto["preço"]
        estoque = produto["estoque"]

        valor_estoque_produto = preço * estoque
        valor_total += valor_estoque_produto

        print(f"Produto: {nome} | Preço: {preço:.2f} | Estoque: {estoque} | Valor total: {valor_estoque_produto:.2f} ")


    print(f"\nValor Total do Estoque: R${valor_total:.2f}")

except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo_json}' não foi encontrado.")
    print("Certifique-se de rodar este script na mesma pasta onde o 'produtos.json' foi criado.")
except KeyError:
    print("Erro: A estrutura do arquivo JSON não possui a chave 'produtos' esperada.")