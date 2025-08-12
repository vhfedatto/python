'''=== Questão ===
Implemente uma tabela hash de tamanho 4.
Insira os seguintes valores: 5, 9, 13, 17, 21, 25.

Utilize o método imprimir() para exibir a estrutura interna da tabela.

Com base na saída, marque a alternativa correta:

a) Todas as posições terão exatamente um valor.
b) A posição 1 conterá os elementos: [5, 9, 13, 17, 21, 25]
c) Todas as chaves cairão na mesma posição, mostrando falha da função hash
d) A posição 1 conterá os elementos: [5, 9, 13, 17, 21, 25] por causa de colisões causadas por valor % 4 == 1
e) O programa gerará erro por excesso de elementos na mesma posição'''

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from hash import HashTable

hashT = HashTable(4)
valores = [5,9,13,17,21,25]

for i in valores:
    hashT.insert(i)

hashT.imprimir()