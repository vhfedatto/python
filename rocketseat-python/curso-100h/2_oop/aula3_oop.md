# LINGUAGEM DE PROGRAMAÇÃO ORIENTADA A OBJETOS

- Organização dos programas em torno de objetos.

> Objetos -> Instâncias de classes.

- Ele é criado a partir da classe. Respeita os métodos e atributos daquela classe.

- Criado para trazer para a programação a forma como enxergamos a realidade.
- Tudo o que você vê no mundo real, você conseguirá colocar como uma classe de código.

> Classe é um modelo - plano que define a estrutura e o comportamento dos objetos.

- Dentro das classes você define os atributos (características) e métodos.
- ```def``` -> dentro de uma classe é um método, fora da classe, é uma função.

```python
class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    
    def saudacao(self):
        return f"Olá, eu sou {self.nome} e tenho {self.idade} anos"

pessoa1 = Pessoa("Victor", 20)

print(pessoa1.saudacao())
```
> *init* -> método padrão - o construtor.

> *self* -> referência a sua própria classe. Porta de acesso para utilizar os métodos e atributos dessa classe.

> "-> None" -> define que esse método não tem retorno.

- Vantagens do POO: Reutilização de código - organiza - clean code.
- Organização e estrutura. Só precisa olhar a classe para entender.
- Agrega complexidade.

## PILARES DA PROGRAMAÇÃO ORIENTADA A OBJETOS

- Estratégias de uso de manipulação das estruturas das classes que vão permitir que você utilize o POO da melhor forma.

### HERANÇA

- Permite criar uma classe que HERDA os atributos e métodos da classe mãe.

```python
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
```

### POLIMORFISMO

- Utilizar o mesmo método da classe-mãe, mas reimplementado de outra forma. Seguindo o mesmo exemplo dos animais.

```python
class Cachorro(Animal):
    def emitir_som(self):
        return "Au, au"
    
class Gato(Animal):
    def emitir_som(self):
        return "Miau!" 
```

> O "emitir_som()" do cachorro é diferente do mesmo método do Gato.

### ENCAPSULAMENTO

- Uso de atributos privados para proteger o dado de ser manipulado de maneira errônea durante o funcionamento do programa.

- Só quem está dentro do contexto que consegue acessar.

> Para definir um atributo privado, basta colocar dois "_" antes do nome dele. Exemplo: "__saldo"

```python
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
```

### ABSTRAÇÃO

> Criar molde para construir as classes

- Classe abstrata não possui implementação, ela é só um molde.
- Tem que passar um decorador para o interpretador entender "isso é uma classe abstrata".

- Quando criar uma classe derivada, utilizando a classe principal, obrigatoriamente ela terá que implementar o método com @abstractmethod. Se não fizer, ela não funcionará.

```python
from abc import ABC, abstractmethod

class Veiculo(ABC):

    @abstractmethod # Obriga a implementação
    def ligar(self):
        pass

    @abstractmethod # Obriga a implementação
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
```
- Se você fosse criar um Avião, teria que ter a implementação do ligar() e desligar(). Isso ajuda na hora do Banco de Dados etc.

## HERANÇA MÚLTIPLA

- Herdar de duas classes. No caso a seguir: Mamifero e Ave.

```python
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
    
class Morcego(Ave, Mamifero):
    def emitir_som(self):
        super().emitir_som() # Não faz diferença aqui. Para Clean code, delete.
        return "Morcegos emitem sons ultrassônicos."

bat = Morcego(nome="Batman")

print("Nome: %s"%bat.nome)
print(f"Som do morcego {bat.emitir_som()}")

# Acessando métodos das classes Mamifero e Ave
print("Morcego amamentando: %s"% bat.amamentar())
print("Morcego voando: %s"% bat.voar())
```

> OBS: quando você chama uma função que já foi definida antes (de quem você está herdando), o python já chama o super(). que pega a implementação original (da classe-mãe), mas se não tiver implementação lá, não faz sentido usar.

## DECORADORES
> Tipo especial de função que permite modificar ou estender o comportamento de outras funções.

> Consegue adicionar funcionalidades a funções e métodos que não precisam alterar o código original da função.

Sintaxe básica:

```python
def meu_decorador(func):
    def wrapper():
        print("Antes da função ser chamada")
        func()
        print("Depois da função ser chamada")
    return wrapper

@meu_decorador
def minha_funcao():
    print("Minha função foi chamada.")

minha_funcao()

# Exemplo: Validar se o usuário está logado
```

Decorador de classe:
```python
from typing import Any

class MeuDecoradorDeClasse:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self) -> Any:
        print("Antes da função ser chamada.")
        self.func()
        print("Depois da função ser chamada.")
        pass

@MeuDecoradorDeClasse
def segunda_funcao():
    print("Segunda função foi chamada")

segunda_funcao()
```

### Exemplos de uso:

Class Method
```python
class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    @classmethod
    def criar_carro(cls, config):
        marca,modelo,ano = config.split(", ")
        return cls(marca, modelo, int(ano))

config1 = "Toyota, Corolla, 2022"
carro1 = Carro.criar_carro(config1)
print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}")
```

Static Method
```python
class Matematica:
    
    @staticmethod
    def somar(a,b):
        return a + b
    
print(Matematica.somar(a=10, b=15))
# Tome muito cuidado com os static method, pois um código cheio deles não é sinal de boa programação. Deixa o código bagunçado e é muito mais difícil de suporte.
```

---

Próxima aula: []()