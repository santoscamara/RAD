
class Task:
    def __init__(self, titulo:str, descricao:str, status: str):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status

    def __str__(self):
        return f"Titulo: {self.titulo}\nDescrição da tarefa: {self.descricao}\nStatus da tarefa: {self.status}\n"
        
    