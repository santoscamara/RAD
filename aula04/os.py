import os


diretorio_arquivo = os.path.dirname(os.path.abspath(__file__))

#Diretorio base
diretorio_base = 'C:\\Users\\aluno\\Desktop\\RAD\\RAD\\aula04'

#subdiretorio e nome do arquivo
subdiretorio = 'RAD\\RAD\\aula03'
nome_arquivo = 'dados.txt'

#construir o caminho relativo
caminho_relativo = os.path.join(diretorio_base, subdiretorio, nome_arquivo)

#obter o caminho absoluto
caminho_absoluto = os.path.abspath(caminho_relativo)

print(f'Caminho relativo: {caminho_relativo}')
print(f'Caminho absoluto {caminho_absoluto}')
print(f'Caminho do arquivo: {diretorio_arquivo}')