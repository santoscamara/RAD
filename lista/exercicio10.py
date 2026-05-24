#Validador de Senhas: Implemente uma regex que valide se uma senha possui: pelo menos 8
#caracteres, uma letra maiúscula, uma minúscula, um número e um caractere especial.

import re

padrao_senha = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
lista_senha = ["12378aB&4", "jaBH83493!", "uu*7dhuaj2", "1278328u", "87q7273Q*"]

for senha in lista_senha:
    if re.match(padrao_senha, senha):
        senha_ocultada = re.sub(padrao_senha, r'********', senha)
        print(f"A senha {senha} informada é uma senha válida")
    else:
        print(f"A senha: {senha} informada não é uma senha válida")
