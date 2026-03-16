#Modo Write

novo = open('C:/Users/iagos/Documents/RAD/aula03/novo.txt', 'w')
novo.write("Iago")
novo.close()

novo = open('C:/Users/iagos/Documents/RAD/aula03/novo.txt')
print(novo.readline())
novo.close()

#Modo Leitura(read)


def ler_arquivo():
    novo = open("C:/Users/iagos/Documents/RAD/aula03/novo.txt")
    print(novo.readline())
    novo.close()


if __name__ == "__main__":
    ler_arquivo()
