"""
IDEIA DO PROGRAMA: DISPUTA DE PENALTIS ENTRE REAL MADRID X BARCELONA

Jogador pode escolher quem bate, onde bate.
Programa decide onde goleiro pula, de defende ou se entra.

"""
from random import randint, choice
from time import sleep

class Player:
    def __init__(self, nome, finalizacao, concentracao, frieza, forca, colocacao):
        self.nome = nome
        self.finalizacao = finalizacao      # precisão geral do chute
        self.concentracao = concentracao    # reduz erro por nervosismo
        self.frieza = frieza                # momentos decisivos
        self.forca = forca                  # dificulta defesa
        self.colocacao = colocacao          # chutes no canto

class Goalkeeper:
    def __init__(self, nome, reflexo, leitura, impulsao):
        self.nome = nome
        self.reflexo = reflexo
        self.leitura = leitura
        self.impulsao = impulsao


real_madrid = [
    Player("Vini Jr", 86, 82, 80, 85, 88),
    Player("Bellingham", 84, 88, 90, 82, 86),
    Player("Mbappé", 92, 85, 88, 91, 90)
]

barcelona = [
    Player("Lewandowski", 91, 87, 90, 86, 89),
    Player("Pedri", 78, 88, 82, 72, 85),
    Player("Raphinha", 83, 80, 78, 84, 82)
]

rma_keeper = Goalkeeper("Courtois", 90, 85, 88)
bar_keeper = Goalkeeper("Ter Stegen", 88, 87, 84)

def loading(text):

    for letter in text:
        print(letter, end="", flush=True)
        sleep(0.5)
    print()

def show_scheme():
    print("._______________.")
    print("| [1]  [2]  [3] |")
    print("| [4]  [5]  [6] |")
    return

def cobrar_penalti(jogador, goleiro, canto_chute):
    canto_goleiro = randint(1, 6)

    chance_chute = (
        jogador.finalizacao * 0.35 +
        jogador.concentracao * 0.2 +
        jogador.frieza * 0.2 +
        jogador.forca * 0.1 +
        jogador.colocacao * 0.15
    )

    chance_defesa = (
        goleiro.reflexo * 0.4 +
        goleiro.leitura * 0.35 +
        goleiro.impulsao * 0.25
    )

    print(f"\n{jogador.nome} bateu no canto {canto_chute}.")
    loading("\n...")
    print(f"{goleiro.nome} pulou no canto {canto_goleiro}.")

        # Primeiro: chance do jogador errar o gol
    teste_chute = randint(1, 100)

    if teste_chute > chance_chute:
        return "Errou para fora!"

    # Segundo: se o goleiro pulou no mesmo canto, pode defender
    if canto_chute == canto_goleiro:
        teste_defesa = randint(1, 100)

        if teste_defesa <= chance_defesa:
            return "Defesa do goleiro!"
        else:
            return "Gol! O goleiro acertou o canto, mas não pegou."

    return "Gol!"

print("="*15+" Menu "+"="*15) #total 21 caracteres base
print("")

teams = ["Real Madrid", "Barcelona"]
count = 0
print(">> Choose your team <<".center(21, "="))
for team in teams:
    count+=1
    print(f"{[count]} {team}")

decision = input("\n[number] ") 

match decision:
    case "1":
        user_team = teams[int(decision)-1]
        print(f"Seu time é o: {user_team}")
    case "2":
        user_team = teams[int(decision)-1]
        print(f"Seu time é o: {user_team}")
    case _:
        print("Invalid number. Try again")

# Escolhe os times com base na decisão do usuário
if user_team == "Real Madrid":
    user_players = real_madrid
    cpu_players = barcelona
    goalkeeper = bar_keeper
else:
    user_players = barcelona
    cpu_players = real_madrid
    goalkeeper = rma_keeper

# Escolher cobrador
print("\nEscolha o cobrador:")
for i, p in enumerate(user_players):
    print(f"[{i+1}] {p.nome}")

while True:
    try:
        escolha = int(input("Número do jogador: "))
        if 1 <= escolha <= len(user_players):
            cobrador = user_players[escolha - 1]
            break
        else:
            print("Escolha inválida. Tente novamente.")
    except:
        print("Digite um número válido.")

show_scheme()

while True:
    try:
        canto = int(input("Escolha onde bater [1-6]: "))
        if 1 <= canto <= 6:
            break
        else:
            print("Escolha inválida. Digite de 1 a 6.")
    except:
        print("Digite um número válido.")

# Executar cobrança
print(f"\nCobrador: {cobrador.nome}")
resultado = cobrar_penalti(cobrador, goalkeeper, canto)

print(f"\nResultado: {resultado}")