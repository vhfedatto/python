"""
IDEIA DO PROGRAMA: DISPUTA DE PENALTIS ENTRE REAL MADRID X BARCELONA

O jogador escolhe:
- qual time vai usar
- quem bate o penalti
- onde bate
- para qual lado o goleiro vai pular para defender
"""

from random import randint, choice
from time import sleep

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
WHITE_BG = "\033[47m"
BLACK = "\033[30m"


class Player:
    def __init__(self, nome, finalizacao, concentracao, frieza, forca, colocacao):
        self.nome = nome
        self.finalizacao = finalizacao
        self.concentracao = concentracao
        self.frieza = frieza
        self.forca = forca
        self.colocacao = colocacao


class Goalkeeper:
    def __init__(self, nome, reflexo, leitura, impulsao):
        self.nome = nome
        self.reflexo = reflexo
        self.leitura = leitura
        self.impulsao = impulsao


real_madrid = [
    Player("Vini Jr", 86, 82, 80, 85, 88),
    Player("Bellingham", 84, 88, 90, 82, 86),
    Player("Mbappe", 92, 85, 88, 91, 90),
    Player("Rodrygo", 85, 81, 84, 83, 86),
    Player("Valverde", 80, 85, 83, 88, 78)
]

barcelona = [
    Player("Lewandowski", 91, 87, 90, 86, 89),
    Player("Pedri", 78, 88, 82, 72, 85),
    Player("Raphinha", 83, 80, 78, 84, 82),
    Player("Yamal", 82, 79, 80, 76, 87),
    Player("Olmo", 84, 84, 83, 79, 85)
]

rma_keeper = Goalkeeper("Courtois", 90, 85, 88)
bar_keeper = Goalkeeper("Ter Stegen", 88, 87, 84)


def loading(text):
    for letter in text:
        print(letter, end="", flush=True)
        sleep(0.2)
    print()


def narrar(texto, cor="", pausa=1.2):
    if cor != "":
        print(colorir(texto, cor))
    else:
        print(texto)
    sleep(pausa)


def colorir(texto, cor):
    return f"{cor}{texto}{RESET}"


def linha(tamanho=54, simbolo="="):
    print(simbolo * tamanho)


def caixa_titulo(texto):
    linha()
    print(colorir(texto.center(54), BOLD + CYAN))
    linha()


def caixa_secao(texto):
    print()
    print(colorir(f"+{'-' * 52}+", YELLOW))
    print(colorir(f"| {texto.center(50)} |", YELLOW))
    print(colorir(f"+{'-' * 52}+", YELLOW))


def show_scheme():
    print(colorir("                GOL", BOLD + BLACK))
    print(colorir("        +-----+-----+-----+", BLUE))
    print(colorir("        |  1  |  2  |  3  |", BLUE))
    print(colorir("        +-----+-----+-----+", BLUE))
    print(colorir("        |  4  |  5  |  6  |", BLUE))
    print(colorir("        +-----+-----+-----+", BLUE))
    print(colorir("        |  7  |  8  |  9  |", BLUE))
    print(colorir("        +-----+-----+-----+", BLUE))


def mostrar_placar(sigla_time_1, placar_time_1, sigla_time_2, placar_time_2):
    texto_time_1 = ", ".join(str(item) for item in placar_time_1)
    texto_time_2 = ", ".join(str(item) for item in placar_time_2)
    gols_time_1 = contar_gols(placar_time_1)
    gols_time_2 = contar_gols(placar_time_2)

    print()
    linha()
    print(colorir("PLACAR DA DISPUTA".center(54), BOLD))
    linha()
    print(f"{colorir(sigla_time_1, BOLD)}  [{texto_time_1}]  {colorir(str(gols_time_1), GREEN + BOLD)}")
    print(f"{colorir(sigla_time_2, BOLD)}  [{texto_time_2}]  {colorir(str(gols_time_2), GREEN + BOLD)}")
    print(colorir("Legenda: ✓ = gol | X = erro | 0 = nao cobrou ainda", CYAN))
    linha()


def contar_gols(lista):
    return lista.count("✓")


def cobrar_penalti(jogador, goleiro, canto_chute, canto_goleiro):
    chance_chute = (
        jogador.finalizacao * 0.35 +
        jogador.concentracao * 0.20 +
        jogador.frieza * 0.20 +
        jogador.forca * 0.10 +
        jogador.colocacao * 0.15
    )

    chance_defesa = (
        goleiro.reflexo * 0.40 +
        goleiro.leitura * 0.35 +
        goleiro.impulsao * 0.25
    )

    narrar(f"\n{jogador.nome} se prepara para a cobranca...", BOLD, 1.3)
    narrar(f"{jogador.nome} bateu no canto {canto_chute}.", BOLD, 1.0)
    loading("...")
    sleep(0.6)
    narrar(f"{goleiro.nome} pulou no canto {canto_goleiro}.", CYAN, 1.2)

    teste_chute = randint(1, 100)
    if teste_chute > chance_chute:
        return "X", "Errou para fora!"

    if canto_chute == canto_goleiro:
        teste_defesa = randint(1, 100)
        if teste_defesa <= chance_defesa:
            return "X", "Defesa do goleiro!"
        return "✓", "Gol! O goleiro acertou o canto, mas nao pegou."

    return "✓", "Gol!"


def escolher_numero(mensagem, minimo, maximo):
    while True:
        try:
            numero = int(input(mensagem))
            if minimo <= numero <= maximo:
                return numero
            print(f"Escolha invalida. Digite um numero de {minimo} a {maximo}.")
        except ValueError:
            print("Digite um numero valido.")


def escolher_cobrador(lista_jogadores, jogadores_usados):
    print(colorir("\nEscolha o cobrador:", BOLD))
    for i in range(len(lista_jogadores)):
        if i not in jogadores_usados:
            print(f"{colorir(f'[{i + 1}]', YELLOW)} {lista_jogadores[i].nome}")

    while True:
        escolha = escolher_numero("Numero do jogador: ", 1, len(lista_jogadores)) - 1
        if escolha not in jogadores_usados:
            jogadores_usados.append(escolha)
            return lista_jogadores[escolha]
        print("Esse jogador ja bateu. Escolha outro.")


def escolher_cobrador_cpu(lista_jogadores, jogadores_usados):
    disponiveis = []
    for i in range(len(lista_jogadores)):
        if i not in jogadores_usados:
            disponiveis.append(i)

    escolha = choice(disponiveis)
    jogadores_usados.append(escolha)
    return lista_jogadores[escolha]


print("=" * 15 + " Menu " + "=" * 15)
teams = ["Real Madrid", "Barcelona"]
caixa_titulo("DISPUTA DE PENALTIS")
print(colorir("          REAL MADRID x BARCELONA", BOLD))
print()
print(colorir("Escolha seu time", YELLOW))

for i in range(len(teams)):
    print(f"{colorir(f'[{i + 1}]', YELLOW)} {teams[i]}")

decision = escolher_numero("\n[number] ", 1, 2)
user_team = teams[decision - 1]
narrar(f"\nSeu time e: {user_team}", GREEN + BOLD, 1.0)

if user_team == "Real Madrid":
    user_players = real_madrid
    cpu_players = barcelona
    user_keeper = rma_keeper
    cpu_keeper = bar_keeper
    user_sigla = "RMA"
    cpu_sigla = "BAR"
else:
    user_players = barcelona
    cpu_players = real_madrid
    user_keeper = bar_keeper
    cpu_keeper = rma_keeper
    user_sigla = "BAR"
    cpu_sigla = "RMA"


placar_usuario = [0, 0, 0, 0, 0]
placar_cpu = [0, 0, 0, 0, 0]

jogadores_usuario_usados = []
jogadores_cpu_usados = []

narrar("\nA disputa vai comecar!", BOLD, 1.3)
mostrar_placar(user_sigla, placar_usuario, cpu_sigla, placar_cpu)
sleep(1.2)

for rodada in range(5):
    caixa_secao(f"RODADA {rodada + 1} DE 5")
    sleep(0.8)

    cobrador = escolher_cobrador(user_players, jogadores_usuario_usados)
    narrar(f"\nSeu cobrador: {cobrador.nome}", GREEN, 1.0)
    show_scheme()
    canto = escolher_numero("Escolha onde bater [1-9]: ", 1, 9)

    simbolo, resultado = cobrar_penalti(cobrador, cpu_keeper, canto, randint(1, 9))
    placar_usuario[rodada] = simbolo
    narrar(f"Resultado: {resultado}", GREEN if simbolo == "✓" else RED, 1.4)
    mostrar_placar(user_sigla, placar_usuario, cpu_sigla, placar_cpu)
    sleep(1.2)

    cobrador_cpu = escolher_cobrador_cpu(cpu_players, jogadores_cpu_usados)
    narrar(f"\nAgora e a vez de {cobrador_cpu.nome} bater para {cpu_sigla}.", BOLD, 1.2)
    show_scheme()
    lado_defesa = escolher_numero(f"Escolha o lado do goleiro {user_keeper.nome} [1-9]: ", 1, 9)

    # O chute do computador e aleatorio. O jogador controla so a defesa.
    simbolo, resultado = cobrar_penalti(cobrador_cpu, user_keeper, randint(1, 9), lado_defesa)
    placar_cpu[rodada] = simbolo
    narrar(f"Resultado: {resultado}", GREEN if simbolo == "X" else RED, 1.4)
    mostrar_placar(user_sigla, placar_usuario, cpu_sigla, placar_cpu)
    sleep(1.4)


gols_usuario = contar_gols(placar_usuario)
gols_cpu = contar_gols(placar_cpu)

caixa_titulo("FIM DA DISPUTA")
narrar(f"Placar final: {user_sigla} {gols_usuario} x {gols_cpu} {cpu_sigla}", BOLD, 1.2)

if gols_usuario > gols_cpu:
    narrar("Voce venceu a disputa de penaltis!", GREEN + BOLD, 1.0)
elif gols_cpu > gols_usuario:
    narrar("O computador venceu a disputa de penaltis!", RED + BOLD, 1.0)
else:
    narrar("A disputa terminou empatada.", YELLOW + BOLD, 1.0)
