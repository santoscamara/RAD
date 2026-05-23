#Dado um arquivo funcionarios.csv (com colunas Nome, Cargo, Salario ), filtre e
#salve em um novo arquivo apenas os funcionários que ganham acima de R$ 5.000.

import csv
import os

caminho = os.path.dirname(os.path.abspath(__file__))
caminho_csv = os.path.join(caminho, 'funcionarios.csv')
caminho_arquivo_filtrado_csv = os.path.join(caminho, 'funcionarios_filtrados.csv')


try:
    with open(caminho_csv, 'r', newline='') as arquivo_origem:
        leitor = csv.DictReader(arquivo_origem)

        filtrados = []

        for linha in leitor:
            salario = float(linha['Salario'])
            
            if salario > 5000:
                filtrados.append(linha)

    with open(caminho_arquivo_filtrado_csv, 'w', newline='') as arquivo_saida:
        campos = ['Nome', 'Cargo', 'Salario']
        escritor = csv.DictWriter(arquivo_saida, fieldnames=campos)

        escritor.writeheader()

        escritor.writerows(filtrados)

    print(f"Sucesso! Arquivo '{arquivo_saida}' gerado com {len(filtrados)} funcionários.")


except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_origem}' não foi encontrado.")
except ValueError:
        print("Erro: Certifique-se de que a coluna 'Salario' contém apenas números válidos (ex: 5500.00).")