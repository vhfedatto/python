'''4. Questão - É preciso contar as Leituras de Corrente Nominal do Motor Acima de um Limite Específico. Escreva um programa em Python que conta quantas leituras de corrente do motor estão acima de um limite específico para cada dia.
Entrada: Matriz (lista 2D) onde cada linha representa um dia e cada coluna representa uma leitura de corrente do motor, juntamente com o limite especificado.
Saída: Lista contendo o número de leituras de corrente do motor que excedem o limite especificado para cada dia.
Dados: Para um limite de 7'''

matriz = [[5.60, 6.07, 4.01, 7.87, 7.76],[6.26, 5.82, 6.28, 7.35, 7.47],[6.89, 7.46, 4.94, 9.68, 9.54],[8.45, 7.86, 8.48, 9.92, 10.09]]
matrizSaida = []

for i in matriz:
    limite = 0

    for j in i:
        if(j > 7):
            limite += 1
    matrizSaida.append(limite)

print("Número de leituras de corrente do motos que excedem o limite específicado:")
for i in range(len(matrizSaida)):
    print(f"{matrizSaida[i]:.2f}")