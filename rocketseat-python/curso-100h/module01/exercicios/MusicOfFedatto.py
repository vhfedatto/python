# Neste arquivo irei colocar tudo o que é ensinado de comandos neste módulo em um código só, ou seja, será totalmente diferente das aulas.
import time

bd = {}
rank = []

print("\n========== FEDATTO'S WORLD ==========\n")
print(">>> Hello! Welcome to the Fedatto's World.\n")

name = input("[+] What is your name?\n> ")
age = int(input("\n[+] What's your age?\n> "))

bd["name"] = name
bd["age"] = age

print("\n-------------------------------------")
print(">>> Oh, so your name is %s!" % name, "Welcome!")
print(">>> I just need to take more information about you...")
print("-------------------------------------\n")

favorite_musics = input("[♪] What is your TOP 3 favorite kinds of music?\n[style 1, style 2, style 3]\n> ").lower().split(", ")

print("\n========== CRITICAL DECISION ==========\n")
print(">>> Okay, but if I said:")
print(">>> 'You have to choose one to be erased from the Universe forever'")
print(">>> Which of these 3 types would you choose?\n")
print(f"Your styles: {favorite_musics}\n")
choise = int(input("[x] Answer (choose 1, 2 or 3):\n> ")) # Não irei fazer tratamento de erros.

favorite_musics.pop(choise-1)

bd["fav_musics"] = favorite_musics

print("\n-------------------------------------")
print(f">>> Ohh... so... these 2 types {favorite_musics} are your favorites.")
print(">>> Buuut now I'm feeling nicer and I'll let you add ANOTHER musical style.")
print("-------------------------------------")

other_music = input("\n[+] What would it be? (JUST ONE!)\n> ").lower()

favorite_musics.append(other_music)

print("\n========== FINAL RANKING ==========\n")
print(">>> So, you like %s too." % other_music)
print(">>> In terms of what you like best, how would you rank these musical styles?\n")

for i in favorite_musics:
    pos = int(input(f"[#] Position for {i}:\n> "))
    rank.insert(pos -1, i)

print("\n========== YOUR TOP MUSIC STYLES ==========\n")
print(f">>> So, your rank is like this: {rank}")

del bd["fav_musics"]
bd["rank"] = rank

# Mostra todas as chaves salvas no dicionário do usuário.
keys_list = list(bd.keys())

# Mostra todos os valores salvos no dicionário do usuário.
values_list = list(bd.values())

# Mostra todos os pares chave e valor salvos no dicionário do usuário.
items_list = list(bd.items())

print("\n========== FEDATTO'S SECRET DATABASE ==========\n")
print(">>> I saved your data in my secret database.")
print(">>> Now you can inspect what exists inside it.\n")
print("[1] Show me the keys")
print("[2] Show me the values")
print("[3] Show me everything")
inspect_mode = int(input("\n[?] Choose 1, 2 or 3:\n> "))

if inspect_mode == 1:
    print(f"\n>>> Database keys: {keys_list}")
elif inspect_mode == 2:
    print(f"\n>>> Database values: {values_list}")
else:
    print(f"\n>>> Full database items: {items_list}")

print("\n>>> Bonus round: now I'll reveal the first registered pair to you.")
print(">>> %s = %s" % (items_list[0][0], items_list[0][1]))

time.sleep(2)

# Mostra o tipo de alguns dados usados no programa.
print("\n========== EXTRA FEATURES ==========\n")
print(f"[type] name -> {type(name)}")
print(f"[type] age -> {type(age)}")
print(f"[type] favorite_musics -> {type(favorite_musics)}")

# Deixa o nome totalmente em letras maiúsculas.
print(f"\n[text] Your name in uppercase: {name.upper()}")

# Conta quantas vezes a letra a aparece no seu nome.
print(f"[text] Letter 'a' appears {name.lower().count('a')} times in your name.")

# Encontra a primeira posição da letra a no seu nome.
print(f"[text] First position of 'a' in your name: {name.lower().find('a')}")

# Converte o nome para bytes e depois volta para texto normal.
name_bytes = name.encode()
print(f"[text] Your name encoded in bytes: {name_bytes}")
print(f"[text] Your name decoded again: {name_bytes.decode()}")

# Verifica se o seu nome começa com a letra V.
print(f"[text] Does your name start with 'V'? {name.upper().startswith('V')}")

print("\n", "-"*73)
print("This project was made by Victor Hugo Fedatto for his 'python' repository.")
print("\nAll rights reserved ©2026\n".center(73))

"""
==================== COMPARAÇÃO COM basics.md ====================

O que eu já aprendi lá e já usei aqui neste arquivo:
- Variáveis.
- int() para converter a idade e as posições do ranking.
- Strings.
- type()
- print().
- input().
- Formatação de texto com %s.
- Formatação de texto com f-string.
- Métodos de texto:
  .lower()
  .split()
  .upper()
  .count()
  .find()
  .encode()
  .decode()
  .startswith()
  in

- Listas.
- Métodos de lista:
  .append()
  .pop()
  .insert()

- Dicionários.
- Métodos de Dicionários:
  del
  .keys()
  .values()
  .items()

- Adição de chave e valor em dicionário, como bd["name"] = name.
- Uso de índices de lista, como pos - 1.

O que do basics.md ainda falta usar aqui e pode virar outro mini projeto/exercício:
- Operações numéricas:
  +
  -
  *
  /
  //
  **
  %
- Mais métodos de texto:
  not in
  .join()
  .replace()
  .strip()
  .rstrip()

- Booleans:
  True
  False
  and
  or
  not

- Mais recursos de listas:
  fatiamento [1:4], [:4], [1:]
  alteração direta por índice
  .index()
  .remove()
  .sort()
- Tuplas e seus métodos:
  .count()
  .index()
"""