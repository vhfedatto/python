import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from estruturaArvore import ArvoreBinaria
from random import randint
import time


#inicio dos códigos:
#01 - Crie uma lista com 50 números aleatórios e em seguida construa uma estrutura de árvore binária, adicione todos os elementos nesta estrutura. Após essas etapas, responda as questões abaixo: Quantos valores impares foram inseridos nesta estrutura? Qual o tempo gasto para construir a árvore? Qual o tempo gasto para imprimir a árvore dentro da estrutura de pré-ordem, in-ordem e pos-ordem?

vetor = [randint(1, 150) for _ in range(50)]
impar = 0

arvore = ArvoreBinaria()

inicio = time.time()
for v in vetor:
  arvore.incluir(v)
fim = time.time()
tempo_execucao = fim - inicio
print(f"O tempo de execução para fazer a árvore foi de {tempo_execucao}")

#pegando os números impares:
for i in vetor:
  if(i % 2 != 0):
    impar +=1

#Pesquisando num vetor normal

#Pré-Ordem
inicio = time.time()
print("\nTravessia Pré-Ordem:")
arvore.pre_order_traversal()
fim = time.time()
tempo_execucao = fim - inicio
print(tempo_execucao)

#Em ordem
inicio = time.time()
print(f"\nTravessia Em Ordem:")
arvore.in_order_traversal()
fim = time.time()
tempo_execucao = fim - inicio
print(tempo_execucao)

#Pós-ordem
inicio = time.time()
print(f"\nTravessia Pós-Ordem:")
arvore.post_order_traversal()
fim = time.time()
tempo_execucao = fim - inicio
print(tempo_execucao)

print(f"\nTem {impar} números impares na Árvore Binária")
 