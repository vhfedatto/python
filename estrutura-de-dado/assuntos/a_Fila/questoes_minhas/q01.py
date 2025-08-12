'''=== Questão ===
Implemente uma fila circular com capacidade 5.
Enfileire os seguintes elementos na ordem: "A", "B", "C", "D", "E"
Depois, desenfileire dois elementos e insira: "F" e "G".
Utilize o método listageral() para exibir o estado final da fila.

Com base na saída final da fila, marque a alternativa correta:

a) A fila está cheia e contém: A → B → C → D → E → F → G → FIM
b) A fila contém: C → D → E → F → G → FIM
c) A fila contém: F → G → C → D → E → FIM
d) A fila contém: G → F → E → D → C → FIM
e) A fila está vazia após duas remoções.'''
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from filaSimples import Fila

fila = Fila(5)
valores = ['A','B','C','D','E']

for i in valores:
    fila.enfileirar(i)

fila.desenfileirar()
fila.desenfileirar()

fila.enfileirar('F')
fila.enfileirar('G')

fila.listageral(
    
)