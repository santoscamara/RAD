from collections import defaultdict

estudantes_por_sala = defaultdict(list)

estudantes_por_sala['B'].append("Jorge")
estudantes_por_sala['A'].append("Jorel")
estudantes_por_sala['A'].append("Joaquim")

print(dict(estudantes_por_sala))