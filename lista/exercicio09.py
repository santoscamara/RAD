#Mascarar Documentos: Crie uma função que localize todos os CPFs ( XXX.XXX.XXX-XX ) em um
#texto e os substitua por ***.***.***- .

import re
padrao_cpf = r'\d{3}\.\d{3}\.\d{3}-(\d{2})'
lista_cpf = ["123.323.234-22", "234.345.234-55", "234.345.645-33", "234.654.643-33"]

def mascarar_cpf(lista_cpf):
    for cpf in lista_cpf:
        substituicao_cpf = re.sub(padrao_cpf,r'***.***.***-\1', cpf)
        print(substituicao_cpf)


if __name__ == "__main__":
    mascarar_cpf(lista_cpf)
