#Atributos do Objeto

texto = open('C:/Users/iagos/Documents/RAD/aula03/texto.txt')
print("Nome do Arquivo: ", texto.name)
print("Tamanho do arquivo posição atual(em bytes): ", texto.tell())
print("Modo do arquvio: ", texto.mode)
print("O arquvio está fechado? ", texto.closed)

texto.close()

print("O arquivo está fechado? ", texto.closed)

