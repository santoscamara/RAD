#Dump de JSON: Crie um dicionário Python com informações de 5 produtos (ID, nome, preço,
#estoque) e salve-o em um arquivo chamado produtos.json com formatação indentada.

import json
import os

caminho = os.path.dirname(os.path.abspath(__file__))
arquivo = os.path.join(caminho, 'produtos.json')

produtos = { 
    "produtos":[
        {"id":1, "nome": "Caneta", "preço": 2.50, "estoque": 2},
        {"id":2, "nome": "Borracha", "preço": 1.50, "estoque": 5},
        {"id":3, "nome": "Lápis", "preço": 2.00, "estoque": 3},
        {"id":4, "nome": "Caderno", "preço": 5.00, "estoque": 6},
        {"id":5, "nome": "Régua", "preço": 6.00, "estoque": 4}
    ]
}

try:
    with open(arquivo, 'w', encoding='utf-8') as arquivo_json:
        json.dump(produtos, arquivo_json, indent=4, ensure_ascii=False)

    print(f"Sucesso! O arquivo {arquivo} foi criado com a formatação indentada.")
except Exception as e:
    print(f"Ocorreu um erro ao salvar o arquivo: {e}")