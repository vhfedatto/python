'''2. Questão - Uma professora armazenou as notas de três provas aplicadas a cinco alunos em uma lista 2D, onde cada linha representa um aluno e cada coluna uma prova.Crie uma lista 2D com os seguintes dados de notas: a) Calcule a média de cada aluno e armazene em uma nova lista. b) Exiba o número do aluno (1 a 5) que obteve a maior média. '''

notas = [[7.0, 8.5, 6.0],[5.5, 6.0, 7.5],[9.0, 9.5, 8.0],[4.0, 5.0, 6.0],[6.5, 7.0, 6.5]]
mediaAlunos = []

for i in notas:
  soma = 0
  for j in i:
    soma+=j
  media = soma / 3
  mediaAlunos.append(media)

indice_maior = 0
for i in range(5):
  print(f"A média do aluno {i+1} foi: {mediaAlunos[i]:.2f}")
  
  if mediaAlunos[i] > mediaAlunos[indice_maior]:
    indice_maior = i

print(f"O aluno com maior média foi o {indice_maior + 1} com média {mediaAlunos[indice_maior]:.2f}")

