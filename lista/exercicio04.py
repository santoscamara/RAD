#Analista de Logs: Crie um programa que leia um arquivo de log ( sistema.log ) e conte quantas
#vezes as palavras "ERROR" e "WARNING" aparecem.

from collections import Counter
import os

caminho = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(caminho, 'sistema.log')


def analisar_log(caminho_arquivo):
   
    contagem = {"ERROR": 0, "WARNING": 0}
    
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                
                contagem["ERROR"] += linha.count("ERROR")
                contagem["WARNING"] += linha.count("WARNING")
                
        print(f"--- Relatório de Análise de Log: {caminho_arquivo} ---")
        print(f"Total de Erros (ERROR): {contagem['ERROR']}")
        print(f"Total de Avisos (WARNING): {contagem['WARNING']}")
        print("-" * 40)

    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        print("Certifique-se de que o arquivo está na mesma pasta do script.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    analisar_log(caminho_arquivo)