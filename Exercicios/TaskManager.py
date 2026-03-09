from Task import Task

class TaskManager():
    def __init__(self):
        self.lista_de_tarefas = []

    def adicionar_tarefa(self,tarefa:Task):
        self.lista_de_tarefas.append(tarefa)

    def listar_tarefas(self):
        for i in range(len(self.lista_de_tarefas)):
                print(f"{self.lista_de_tarefas[i]}")
    
    def check_tarefa(self,tarefa:Task): 
        check = input(f"A tarefa {tarefa.titulo} foi concluída?(Sim ou Não) \n")
        if check == "Sim":
              tarefa.status = "Sim"
        elif check == "Não":
              tarefa.status = "Não"
        
    




