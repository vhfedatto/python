import random

class Jogador:
    def __init__(self, nome, finalizacao, concentracao, frieza, forca, colocacao):
        self.nome = nome
        self.finalizacao = finalizacao
        self.concentracao = concentracao
        self.frieza = frieza
        self.forca = forca
        self.colocacao = colocacao

    def cobrar_penalti(self):
        chance_gol = (
            self.finalizacao * 0.4 +
            self.concentracao * 0.2 +
            self.frieza * 0.2 +
            self.forca * 0.1 +
            self.colocacao * 0.1
        )

        resultado = random.randint(1, 100)

        if resultado <= chance_gol:
            return "Gol ⚽"
        else:
            return "Errou ❌"


# Criando jogadores
jogador1 = Jogador("Neymar", 90, 85, 95, 80, 92)
jogador2 = Jogador("Zagueiro Aleatório", 60, 50, 40, 70, 55)

# Testando cobranças
print(f"{jogador1.nome} cobrando pênalti...")
print(jogador1.cobrar_penalti())

print("\n-------------------\n")

print(f"{jogador2.nome} cobrando pênalti...")
print(jogador2.cobrar_penalti())