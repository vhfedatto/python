import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from filaSimples import Fila

#inicio dos códigos:
#LEMBRAR DE TROCAR DTYPE PARA OBJECT!!

fila1 = Fila(4)
fila1.enfileirar('Carro A')
fila1.enfileirar('Carro B')
fila1.enfileirar('Carro C')
fila1.enfileirar('Carro D')

fila1.listageral()

fila2 = Fila(4)
fila2.enfileirar('Carro A')
fila2.enfileirar('Carro B')

fila2.desenfileirar()

fila2.enfileirar('Carro C')
fila2.enfileirar('Carro D')

print('\n== A e B entram, A sai ==')
fila2.listageral()