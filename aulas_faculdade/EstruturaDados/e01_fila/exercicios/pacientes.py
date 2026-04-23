import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from filaSimples import Fila

# Inicializa filas separadas
prioridade1 = Fila(100)        # 80+
prioridade2 = Fila(100)        # 60 a 79
sem_prioridade = Fila(100)     # <60

while True:
    num = int(input('Quantos pacientes queres adicionar? [0 para sair] '))

    if num == 0:
        break

    for i in range(num):
        idade = int(input(f'Idade do Paciente {i+1}: '))
        
        if idade >= 80:
            prioridade1.enfileirar(idade)
        elif idade >= 60:
            prioridade2.enfileirar(idade)
        else:
            sem_prioridade.enfileirar(idade)

print("\n=== Ordem de Atendimento ===")
print("Prioridade 1 (80+):")
while not prioridade1.fila_vazia():
    print(f"Atendendo paciente com idade: {prioridade1.desenfileirar()}")

print("\nPrioridade 2 (60 a 79):")
while not prioridade2.fila_vazia():
    print(f"Atendendo paciente com idade: {prioridade2.desenfileirar()}")

print("\nSem prioridade (<60):")
while not sem_prioridade.fila_vazia():
    print(f"Atendendo paciente com idade: {sem_prioridade.desenfileirar()}")