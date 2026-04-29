# @classmethod
# @staticmethod

class MinhaClasse:
    valor = 10 # Atributo de classe

    def __init__(self, nome) -> None:
        self.nome = nome #atributo da instância
    
    # Requer uma instância para ser chamado.
    def metodo_instancia(self):
        return f"Método de instância chamado para {self.nome}"
    
    @classmethod # Não precisa de uma instância para ter acesso aos atributos e métodos
    def metodo_classe(cls):
        return f"Método da classe chamado para valor={cls.valor}"
    
    @staticmethod # Não tem acesso aos atributos e métodos da instância.
    def metodo_estatico(): # Executa uma função específica
        return "Método estático chamado"
    
obj = MinhaClasse(nome="Classe Exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor) #Não precisa de instância para acessar um atributo da classe.
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())



# Onde vai usar?

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


# Outro exemplo:

class Matematica:
    
    @staticmethod
    def somar(a,b):
        return a + b
    
print(Matematica.somar(a=10, b=15))
# Tome muito cuidado com os static method, pois um código cheio deles não é sinal de boa programação. Deixa o código bagunçado e é muito mais difícil de suporte.