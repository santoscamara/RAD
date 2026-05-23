from pessoa import Pessoa
from marca import Marca

class Veiculo:
    def __init__(self, placa: str, cor: str, proprietario: Pessoa, marca: Marca)->None:
        self.placa = placa
        self.cor = cor
        self.proprietario = proprietario
        self.marca = marca

    def __str__(self):
        return f"Placa: {self.placa}, cor: {self.cor}, Cpf do proprietario: {self.proprietario.cpf}, Id da marca: {self.marca.id}"