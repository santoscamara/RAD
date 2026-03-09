from Aluno import Aluno
from Task import Task
from TaskManager import TaskManager


if __name__ == "__main__":
    aluno1 = Aluno("João", 22, [5.0, 7.0, 8.0])
    aluno2 = Aluno("Maria", 25, [8.0, 8.2, 6.0])
    alunos = [aluno1, aluno2]
    for aluno in alunos:
        print(f"Nome: {aluno.nome}, Idade: {aluno.idade}, Média: {aluno.calcular_media():.2f}")
    tarefa1 = Task("Varrer a Casa", "Limpeza da casa com a vassoura", "Não")
    tarefa2 = Task("Lavar a Louça", "Realização da limpeza da louça do dia", "Sim")
    tarefa3 = Task("Estudar Python", "Estudar os conceitos e paradigmas de Python", "Sim")
    gerenciador_de_tarefas = TaskManager()
    gerenciador_de_tarefas.adicionar_tarefa(tarefa1)
    gerenciador_de_tarefas.adicionar_tarefa(tarefa2)
    gerenciador_de_tarefas.adicionar_tarefa(tarefa3)
    gerenciador_de_tarefas.listar_tarefas()
    gerenciador_de_tarefas.check_tarefa(tarefa1)
    gerenciador_de_tarefas.check_tarefa(tarefa2)
    gerenciador_de_tarefas.check_tarefa(tarefa3)
    print(tarefa1)
    print(tarefa2)
    print(tarefa3)
    
   
    
