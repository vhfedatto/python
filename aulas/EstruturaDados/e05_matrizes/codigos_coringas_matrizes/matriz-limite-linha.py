# Esse código serve para problemas que peçam para verificar algum número dentro de uma linha e ver se é maior ou menor

matriz = [[1, 3], [5, 5], [0, 10], [3, 4]]
matrizSaida = []

for i in matriz:
   limite = 0 #modificar o limite para o número apresentado na questão
   for j in i:
     if(j >= 7):
        limite+=1 #adiciona sempre que excede
        matrizSaida.append(limite)

print("Número de leituras que excedem o limite específicado: ")

for i in range(len(matrizSaida)):
   print(f"{matrizSaida[i]:.2f}")