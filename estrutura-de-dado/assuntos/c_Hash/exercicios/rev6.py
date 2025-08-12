'''6 - Questão - Uma escola está cadastrando os alunos para um novo sistema. Cada aluno possui um identificador numérico único. Como o número total de alunos é grande, a escola decide utilizar uma tabela hash para facilitar buscas, inserções e exclusões de alunos.
Tarefa:
> Implemente uma HashTable com tamanho 5.
> Insira os seguintes identificadores de alunos: 101, 202, 303, 404, 505, 606
> Imprima a tabela hash após as inserções.
> Remova o identificador 303 e imprima novamente.
> Tente buscar o aluno 505 e mostre a posição onde ele foi armazenado.'''

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from hash import HashTable

#a
hashTable = HashTable(5) #tamanho conforme requisitado

#b
hashTable.insert(101)
hashTable.insert(202)
hashTable.insert(303)
hashTable.insert(404)
hashTable.insert(505)
hashTable.insert(606)

#c
hashTable.imprimir()

#d
print(f"{'-'*20}\nd)")
hashTable.remove(303)
hashTable.imprimir()

#e
print(f"{'-'*20}\ne)")
aluno = int(input("No. Aluno: "))

try:
    index = hashTable.get(aluno)
    print(f"O aluno {aluno} está no index:", index)
except:
    print(f"O aluno {aluno} não existe")