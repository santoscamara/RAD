from datetime import date

class Pessoa:
    def __init__(self, cpf:str, nome:str, nascimento: date, oculos: bool)->None:
        self.cpf = cpf
        self.nome = nome
        self.nascimento = nascimento
        self.oculos = oculos


    def __str__(self):
        return f"Pessoa: {self.nome}, cpf: {self.cpf}, nascimento: {self.nascimento}, usa óculos: {self.oculos}"
    