def criar_registro (arquivo):
    with open(arquivo, "w") as file:
        file.write("Registro de notas dos alunos\n")
        file.write("-----------------------------\n")

def adicionar_notas (arquivo, aluno, nota):
    with open(arquivo, "a") as file:
        file.write(f"Aluno: {aluno}\n")
        file.write(f"Nota: {nota}\n")
        file.write("-----------------------------\n")

if __name__ == "__main__":
    registro_notas = "registro_notas.txt"
    criar_registro(registro_notas)
    adicionar_notas(registro_notas, "Julio", 8)
    adicionar_notas(registro_notas, "Cesar", 7)
    adicionar_notas(registro_notas, "Carlos", 9)
    adicionar_notas(registro_notas, "Pedro", 6)