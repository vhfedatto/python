'''7 - Questão - Um sistema de atendimento médico utiliza senhas numéricas para organizar o atendimento dos pacientes. Para otimizar a distribuição e localização das senhas, um algoritmo de tabela hash é usado.
Tarefa:
> Crie uma tabela hash de tamanho 7.
> Insira as senhas chamadas no dia: 14, 21, 28, 35, 1, 8, 15.
> Mostre o estado da tabela após as inserções.
> Faça a remoção da senha 21 e tente acessar novamente essa senha (trate o erro com try/except).
> Por que a maioria dos elementos foi parar na mesma posição da tabela? O que isso diz sobre a função hash utilizada?'''

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from hash import HashTable

#a
hashTable = HashTable(7) #Tamanho na questão

#b
hashTable.insert(14)
hashTable.insert(21)
hashTable.insert(28)
hashTable.insert(35)
hashTable.insert(1)
hashTable.insert(8)
hashTable.insert(15)

#c
hashTable.imprimir()

#d
print(f"{'-'*20}\nd)")
hashTable.remove(21)
senha = int(input(">> Digite a senha: "))

try:
    index = hashTable.get(senha)
    print(f"A senha {senha} está no index: {index}")
except:
    print(f">>A senha {senha} não pôde ser encontrada!<<")

#e
# O números adicionados no index 0 são múltiplos de 7, no index 1 são múltiplos de 7+1 e assim por diante;
# A função hash no caso aqui seria hash(x) = x % 7 [tamanho]. 
# Isso mostra que a função hash está mal adaptada para esse conjunto de dados - o ideal seria ajustar o tamanho da tabela ou a função hash para obter melhor dispersão.