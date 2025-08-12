'''=== Questão ===
Crie uma tabela hash com tamanho 5 e insira os seguintes valores: 10, 15, 20, 25, 30, 3.
Em seguida, imprima a tabela com o método imprimir().

Com base na saída do método imprimir(), marque a alternativa correta:
a) Posição 0: [10, 15, 20, 25, 30, 3]
b) Posição 3: [3], Posição 0: [10, 15, 20, 25, 30]
c) Posição 0: [10, 15, 20, 25, 30], Posição 3: [3]
d) Posição 3: [10, 15, 20, 25, 30], Posição 0: [3]
e) Posição 1: [10, 15], Posição 2: [20, 25], Posição 3: [30, 3]'''
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from hash import HashTable

hashTable = HashTable(5)
valores = [10, 15, 20, 25, 30, 3]

for i in valores:
    hashTable.insert(i)

hashTable.imprimir()