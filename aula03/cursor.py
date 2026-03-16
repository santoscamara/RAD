#Cria um arquivo exemplo e escreve nele
with open("C:/Users/iagos/Documents/RAD/aula03/exemplo.txt", 'w', encoding='utf-8') as f:
    f.write("Exemplo de uso dos metodos seek() e tell() em Python.")

#Le o arquivo e usa seek() e tell()
with open("exemplo.txt", 'r', encoding = 'utf-8') as f:
    print('Posição inicial do cursor: ', f.tell())

    conteudo = f.read(10)
    print("Conteudo lido:", conteudo)
    print("Posição do cursor após ler 10 caracteres:", f.tell())


    f.seek(0,0) #whence = 0: inicio do arquivo
    print('Posição do cursor após seek(0,0):', f.tell())
