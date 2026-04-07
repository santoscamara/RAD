from collections import Counter

a = "Uma serie de palavras aleatorias".split()
contagem = Counter(a)

print(contagem)
print(contagem.most_common(4))