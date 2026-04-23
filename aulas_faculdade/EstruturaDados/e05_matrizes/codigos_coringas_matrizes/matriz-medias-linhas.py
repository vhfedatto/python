##Esse código serve para programas que peçam para calcular média das linhas:

matriz = [[1, 3], [5, 5], [0, 10], [3, 4]]
matrizSaida = []

for i in matriz:
    soma = 0
    c= 0
    for j in i:
        soma+=j
        c+=1
    media = soma / c
    matrizSaida.append(media)

#Imprimindo...
print("A média de saída é:")

for i in range(len(matrizSaida)):
    print(f"{matrizSaida[i]:.2f}")