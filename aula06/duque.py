from collections import deque

historico = deque(maxlen=3)

historico.append("página 1")
historico.append("página 2")
historico.append("página 3")
print(f"Histórico atual: {historico}")

historico.append("página 4")
print(f"Após nova página: {historico}")

fila = deque(["Caroline", "Samira", "Juliana"])

fila.appendleft("Mayara")

ultimo = fila.pop()
print(f"fila final: {fila}")
print(f"Quem saiu por último: {ultimo}")