# Função da fórmula de Bhaskara
import math
# Funções:
def bhaskara(a, b, c):
    delta = b**2 - 4 * a * c
    if delta < 0:
        return None, None
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    return x1, x2

def soma_x1_x2(x1, x2):
    return x1 + x2

def lista_positiva(valor):
    return list(range(0, int(valor) + 1))

def lista_negativa(valor):
    return list(range(-1, int(valor + 2) - 1)) 

def lista_negativa_zero(valor):
    return list(range(int(valor), 1))

# Programa Principal
a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))

x1, x2 = bhaskara(a, b, c)

if x1 is None or x2 is None:
    print('Não há raízes reais.')
else:
    soma = soma_x1_x2(x1, x2)
    print(f"\nAs raízes são x1 = {x1} e x2 = {x2}")
    print(f"A soma das raízes é: {soma}")

    if soma > 0 and soma % 2 == 0:
        lista_resultado = lista_positiva(soma)
        print(f"Lista de valores positivos de 0 até {soma}: {lista_resultado}")
    elif soma > 0 and soma % 2 != 0:
        lista_resultado = lista_negativa(soma)
        print(f"Lista de valores negativos de -1 até {int(soma)}: {lista_resultado}")
    else:
        lista_resultado = lista_negativa_zero(soma)
        print(f"Lista de valores negativos de {soma} até 0: {lista_resultado}")

        