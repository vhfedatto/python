#questão 4 - dicionários grupos

masculino={}
feminino={}
decisao='S'
contador_masc = 1
contador_fem = 1

print('Sistema de cadastro de clientes usando Dicionário - responda as perguntas corretamente.')
while decisao == 'S':
    sexo = input("Qual o sexo do cliente? [masculino/feminino] ").lower()
    nome = input("Qual o nome do cliente? ")
    idade = int(input("Qual a idade do cliente? "))
   
    if sexo == "masculino" or sexo == "m":
        masculino[f"cliente {contador_masc}"] = {"nome": nome, "sexo": "masculino", "idade": idade}
        contador_masc += 1
    
    elif sexo == "feminino" or sexo == "f":
        feminino[f"cliente {contador_fem}"] = {"nome": nome, "sexo": "feminino", "idade": idade} 
        contador_fem += 1                
    
    decisao = input('Deseja continuar? [S/N]: ').upper()

print("As clientes femininas são:")
for chave, dados in feminino.items():
    print(f"{chave}: {dados['nome']}, {dados['sexo']}, {dados['idade']}")
print()
print("Os clientes masculinos são:")
for chave, dados in masculino.items():
    print(f"{chave}: {dados['nome']}, {dados['sexo']}, {dados['idade']}")
print()
print(feminino)
print(masculino)

