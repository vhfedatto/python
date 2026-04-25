#Lista - aplicar 10%

lista = [1000, 1500, 1250, 2500]

def imposto(lista):
    nova_lista = [] 
    for i in lista:
        novo_valor = i * 1.10  
        nova_lista.append(novo_valor) 
    print(nova_lista)

imposto(lista)

