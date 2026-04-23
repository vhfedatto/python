import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from filaSimples import Fila

#inicio dos códigos:
#LEMBRAR DE TROCAR DTYPE PARA OBJECT!!

filaAnimais = Fila(4)

filaAnimais.enfileirar('Cachorro (10h)')
filaAnimais.enfileirar('Gato (10h15)')
filaAnimais.enfileirar('Coelho (10h30)')
filaAnimais.enfileirar('Papagaio (10h45)')

print('\n=== Fila ===')
filaAnimais.listageral()

atendido1 = filaAnimais.desenfileirar()
atendido2 = filaAnimais.desenfileirar()

print("\n=== Animais atendidos ===")
print(atendido1)
print(atendido2)

print('\n=== Fila após alguns atendimentos ===')
filaAnimais.listageral()