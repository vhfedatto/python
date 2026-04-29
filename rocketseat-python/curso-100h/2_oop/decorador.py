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

# De Classe
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