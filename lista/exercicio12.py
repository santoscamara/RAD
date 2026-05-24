#Palíndromo: Desenvolva uma função que receba uma frase, remova os espaços e pontuações,
#e verifique se ela é um palíndromo (lê-se igual de trás para frente).


import re

def palindromo(frase:str):
    frase_limpa = frase.lower()

    frase_limpa = re.sub(r'[^\w]|_','',frase_limpa)
    
    return frase_limpa == frase_limpa[::-1]


if __name__ == "__main__":
    frases_teste = [
            "Aara",
            "A base do teto desaba.",
            "Ame o poema.",
            "A cara rajada da jararaca.",
            "A rará rará rará.", 
            "O romano acata o amor a damasco e o mesmo romaneia.",
            "Python não é palíndromo"
        ]
    
    for frase in frases_teste:
        resultado = "É palindromo!" if palindromo(frase) else "Não é um palindromo."
        print(f"{frase} -> {resultado}")
