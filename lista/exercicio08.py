#Extração de Telefones: Escreva um programa que use re.findall() para extrair todos os
#números de telefone no formato (XX) 9XXXX-XXXX de um texto longo

import re

padrao_telefone = r'\([0-9]{2}\)\s?9[0-9]{4}-[0-9]{4}'
lista_telefone = ["(21)94365-4324", "44 94234-444", "(53) 94234-4243", "(22)8298-8928"]

def validar_telefone(lista_telefone):
    for telefone in lista_telefone:
        if re.findall(padrao_telefone, telefone):
            print(f"O telefone {telefone} é um número válido")
        else:
            print(f"O telefone {telefone} não é um número válido")

if __name__ == "__main__":
    validar_telefone(lista_telefone)

