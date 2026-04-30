from os import system
from random import randint, shuffle


def add_team(teams):
    print("\nQuantos times queres adicionar? ")
    n = converter_valor(input("[num] "))

    if n is None:
        print("Digite um número válido.")
        return
       
    print(f"\nAdicione os {n} times")
    
    for i in range(n):
        time = input("[+] ")
        teams.append(time)
    
    system('cls')

def converter_valor(n):
    try:
        return int(n)
    
    except ValueError:
        return None

def show_teams(teams):
    c = 1
    print("Os times adicionados, foram:")
    
    for i in teams:
        print(f"{[c]} {i}")
        c+=1
    print("")

def sortear(teams):
    
    if len(teams) not in [4, 8, 16]:
        print("Número de times inválido. Precisa ser 4, 8 ou 16")
        return

    shuffle(teams)

    print("Confrontos sorteados:")
    for i in range(0, len(teams), 2):
        print(f"{teams[i]} x {teams[i+1]}")
    
    input("Press 'Enter' to clear the terminal")
    system('cls')


teams = []
# teams ["RST", "BRI", "KRO", "MYV", "HOL", "KVI", "DSV", "CVW"]

while True:
    print("="*25+" SORTEADOR "+"="*25)
    print("[1] Adicionar time\n[2] Ver times\n[3] Sortear\n[4] Sair do programa")
    escolha = input("\n[opt] ")

    match escolha:
        case "1":
            add_team(teams)
        
        case "2":
            show_teams(teams)

        case "3":
            sortear(teams)
        
        case "4":
            exit




