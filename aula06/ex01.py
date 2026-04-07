import re

PADRAO_EMAIL = re.compile(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')

def validar_email(email):
    return bool(PADRAO_EMAIL.match(email))

if __name__ == "__main__":
    exemplos_emails = [
    "usuario@email.com",    # valido
    "nome+tag@email.com",   # invalido
    "a@b.co",               # valido, dominio curto
    "usuario@email.co.uk",  # valido
    "@email.com",           # invalido, sem usuario
    "usuario@.com",         # invalido
    "usuario@email",        # invalido, sem TLD(Top-Level Domain)
    "usu ario@email.com",   # invalido, espaço
    ]
    for email in exemplos_emails:
        if validar_email(email):
            print(f"{email} é um endereço de e-mail válido. ")
        else:
            print(f"{email} não é um endereço de e-mail válido. ")
