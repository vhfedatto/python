'''=== Questão ===
Crie uma matriz 3x3 com os seguintes números:
[[2, 4, 6],
 [1, 3, 5],
 [7, 8, 9]]
a) Calcule e exiba a soma dos elementos de cada coluna e armazene em uma nova lista.
b) Depois, exiba o índice da coluna que teve a maior soma.

Com base nos valores obtidos, marque a alternativa correta:

a) A coluna de maior soma foi a 0.
b) A coluna de maior soma foi a 1.
c) A coluna de maior soma foi a 2.
d) Todas as colunas têm a mesma soma.
e) A coluna de maior soma foi a que tem os números [1, 3, 5].'''

valores = [[2, 4, 6],[1, 3, 5],[7, 8, 9]]
soma = [0,0,0]

# Percorre cada linha
for i in valores:
    for j in range(len(i)):
        soma[j] += i[j]

print("Soma das colunas: ", soma)

index_maior = soma.index(max(soma))
print("Coluna com a maior soma foi: ",index_maior)