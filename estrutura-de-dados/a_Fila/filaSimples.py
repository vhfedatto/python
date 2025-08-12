import numpy as np

class Fila:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype = object)

    def fila_vazia(self):
        return self.numero_elementos == 0
    
    def fila_cheia(self):
        return self.numero_elementos == self.capacidade
    
    def enfileirar(self, valor):
        if self.fila_cheia():
            print('A fila está cheia')
            return
        if self.final == self.capacidade - 1:
            self.final = -1
        
        self.final +=1
        self.valores[self.final] = valor
        self.numero_elementos +=1
    
    def desenfileirar(self):
        if self.fila_vazia():
            print('A fila já está vazia')
            return
        temp = self.valores[self.inicio]
        self.inicio +=1
        if self.inicio == self.capacidade - 1:
            self.inicio = 0
        else:
            self.numero_elementos -= 1
            return temp
    
    def primeiro(self):
        if self.fila_vazia():
            return -1
        else:
            return self.valores[self.inicio]
        
    def visualizar(self):
        print('Tamanho da Fila..: ', self.capacidade)
        print('Início da fila...: ', self.inicio)
        print('Final da fila....: ', self.final)
        print('Variável Nu. El..:', self.numero_elementos)

    def listageral(self):  #criado por mim - o do professor está errado
        print("Fila atual:")
        index = self.inicio
        count = 0
        while count < self.numero_elementos:
            print(self.valores[index], end=' -> ')
            index = (index + 1) % self.capacidade
            count += 1
        print("FIM")


"""fila1 = Fila(4) #criando a lista
fila1.enfileirar(9) #enfileirando o número 9 na posição inicial
fila1.enfileirar(5)
fila1.enfileirar(2)
fila1.enfileirar(1) #ultima posição

fila1.desenfileirar() #desenfileirando o primeiro número (9)

print('O primeiro na fila é: ', fila1.primeiro()) #print do primeiro número"""