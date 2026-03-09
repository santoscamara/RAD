from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    idade: int
    notas: list

    def calcular_media(self):
        for i in range(len(self.notas)):
            if self.notas[i] < 0 or self.notas[i] > 10:
                raise ValueError(f"Nota {self.notas[i]} Inválida")   
        return sum(self.notas)/len(self.notas)




    
