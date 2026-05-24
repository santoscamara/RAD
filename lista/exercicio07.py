#Validador de E-mail: Crie uma função que utilize Regex para verificar se uma string enviada
#pelo usuário é um e-mail válido

import re

def validar_email(email):
    regex_padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(regex_padrao, email):
        return True
    else:
        return False
    

if __name__ == "__main__":
    lista_email = [
        "usuario@email.com",
        "joao.silva123@empresa.com.br",
        "suporte-tecnico@dominio.org",
        "email_invalido.com",       
        "jose@dominio",             
        "maria@.com",               
        " @espaco.com",
    ]

    for email in lista_email:
        if validar_email(email):
            print(f"O e-mail '{email}' é valido")
        else:
            print(f"O e-mail '{email}' não é valido")