#Extração de URLs: Escreva um script que identifique e liste todas as URLs ( http:// ou
#https:// ) presentes em uma string de texto.
import re

padrao_url = r'https?://[^\s]+'

lista_url = ["http://www.google.com", "https://www.yahoo.com.br", "www.globo.com", "x.com"]

for url in lista_url:
    if re.findall(padrao_url, url):
        print(f"O site {url} é um url válido")
    else:
        print(f"O site {url} não é um site válido")