'''=== Questão ===
Implemente uma tabela hash com tamanho 6.
Insira os seguintes valores: 12, 18, 24, 30, 7, 13
Após isso:

a) Remova o número 18
b) Peça para o usuário digitar um número e busque-o na tabela usando o método get().
c) Exiba a posição onde ele foi encontrado ou uma mensagem de erro, se não estiver presente.

Sabendo que o usuário digitou o número 18, marque a alternativa correta sobre o que será exibido no console:

a) A senha 18 está no index: 0
b) >>A senha 18 não pôde ser encontrada!<<
c) A senha 18 está no index: 6
d) Posição 0: [12, 18, 24, 30], então a busca retornará sucesso
e) Não é possível buscar uma senha após a remoção'''

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from hash import HashTable

hashT = HashTable(6)
valores = [12,18,24,30,7,13]

for i in valores:
    hashT.insert(i)

hashT.imprimir()

hashT.remove(18)

busca = int(input("Busque um número: "))
try:
    index = hashT.get(busca)
    print(f"A senha {busca} está no index {index}")
except:
    print(f">> A senha {busca} não está no Hash <<")