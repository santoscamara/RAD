## ms9.py

import re
#re=regex
def verifica_regex(texto: str) -> None:
    padrao = r"\(\d{3}\) \d{3}-\d{4}"
    #Padrao para encontrar numeoros de telefone no formato (XXX) XXX-XXXX
    resultado = re.search(padrao, texto)
    if resultado:
        numero_telefone = resultado.group()
        print("Número de telefone encontrado:", numero_telefone)
    else:
        print("Número de telefone não encontrado.")

if __name__ == "__main__":
    verifica_regex("O número de telefone do Mathias é (123) 456-7890.")
