'''5 - Questão - Uma loja controla o estoque de 3 produtos em 4 filiais diferentes usando uma matriz. Cada linha representa uma filial e cada coluna um produto. Dada a seguinte lista:
a) Calcule o total de produtos em cada filial.
b) Calcule o total de cada produto em todas as filiais.
c) Exiba qual filial tem o menor número de produtos no total.'''

matriz = [[10, 5, 8],[3, 7, 2],[6, 2, 4],[9, 1, 3]]
matrizTotal = []
matrizPProd = [0] * len(matriz[0])

#Total por filial
for i in matriz:
    soma = 0
    for j in i:
        soma += j
    matrizTotal.append(soma)

#Total por produto:
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matrizPProd[j] += matriz[i][j]

#A - total
for i in range(len(matriz)):
    print(f"Total de produtos na filial {i+1}: {matrizTotal[i]}")

print(f"{'-'*50}")

#B - por produto
for i in range(len(matrizPProd)):
    print(f"Produto {i+1} possui nas filiais o estoque total de: {matrizPProd[i]}")

print(f"{'-'*50}")

#C - Menor loja
indice = 0
for i in range(len(matriz)):
    if matrizTotal[i] < matrizTotal[indice]:
        indice = i
print(f"A loja que tem menos produtos é a loja {indice+1}")
print(f"{'-'*50}")