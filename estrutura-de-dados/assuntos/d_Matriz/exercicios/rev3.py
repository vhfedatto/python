'''3. Questão - É preciso calcular a média de Temperatura do Óleo por Semana. Desenvolva um programa em Python que calcula a média da temperatura do óleo para cada semana.
Entrada: Matriz (lista 2D) onde cada linha representa uma semana e cada coluna representa uma leitura de temperatura do óleo.
Saída: Lista contendo a média da temperatura do óleo para cada semana. '''

matriz = [[75.59,64.00,63.59,68.84,72.94], [62.40,64.72,73.57,70.33,63.87], [92.98,78.72,78.22,84.67,89.71], [84.24,87.38,99.31,94.95,86.22]]
matrizSaida = []

for i in matriz:
    soma = 0 
    c= 0
    
    for j in i:
      soma+=j
      c+=1
      media = soma / c
      matrizSaida.append(media)
      
print("A média das temperaturas é:")

for i in range(len(matrizSaida)):
   print(f"{matrizSaida[i]:.2f}")