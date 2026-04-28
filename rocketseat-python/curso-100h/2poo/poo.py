class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    
    def saudacao(self):
        return f"Olá, eu sou {self.nome} e tenho {self.idade} anos"


pessoa1 = Pessoa("Victor", 20)

print(pessoa1.saudacao())

# Exemplo de Herança:

class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def andar(self):
        return f"O animal {self.nome} andou"
    
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au, au"
    
class Gato(Animal):
    def emitir_som(self):
        return "Miau!"
    
dog = Cachorro(nome="Rex")
cat = Gato(nome="Felix")

# Polimorfismo
animais = [dog, cat]

for i in animais:
    print(f"{i.nome} faz: {i.emitir_som()}")


# Encapsulamento
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo # Atributo Privado
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(saldo = 1000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=500)

print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=500)

print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.sacar(valor=200)

print(f"Saldo da conta bancária: {conta.consultar_saldo()}")



# Abstração

from abc import ABC, abstractmethod

class Veiculo(ABC):

    @abstractmethod # Obriga a implementação nos herdeiros
    def ligar(self):
        pass

    @abstractmethod # Obriga a implementação nos herdeiros
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self) -> None:
        pass
    
    def ligar(self):
        return "Carro ligado usando a chave."
    
    def desligar(self):
        return "Carro desligado usando a chave."

carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())



## Herança Multipla

class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} está amamentando."
    
class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando."