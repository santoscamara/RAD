class Marca:
    def __init__(self, id: int, nome: str, sigla: str) -> None:
        self.id = id
        self.nome = nome
        self.sigla = sigla

    def __str__(self):
        return f"Id: {self.id}, Nome: {self.nome}, Sigla: {self.sigla}"