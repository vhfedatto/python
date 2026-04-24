# ROCKETSEAT - PYTHON
Professor: Gabriel Casemiro Rocketseat
Aluno: Victor H Fedatto Vasconcelos

```OBS: Alguns conceitos básicos da linguagem eu não vou focar tanto, pois eu já sou intermediário em Python (e estou fazendo o curso do 0 até o avançado).```

## What is Python?

- Linguagem de programação ORIENTADA A OBJETO;
- Alto nível (se aproxima da linguagem humana);
- Tipagem Dinâmica e forte;
- Interativa e Interpretada;
- Muito fácil de se programar.

Python é interpretado por byteCode por meio do REPL (interpretador dele), tornando possível a portabilidade do código.

- Criado em 1990 no Instituto de Pesquisa na Holanda.

## LECTURE 01 (30 videos) - LEARNING BY DOING

### 1. Terminal & Sintax

- ls -> listagem de pastas da sua pasta.
- dir -> listagem de todas as pastas disponíveis;
- cd -> change disk -> entrar e sair de pastas;

```python
.center(n) # -> n = número de caracteres -> alinha o texto dentro desse espaço n no terminal :)
```

- Sintaxe: Conjunto de regras que vai regir como você pode escrever os programas -> Se não seguir: Compilador não entende e dá um "Sintaxe error".

###  2. VARIABLES

- Não pode: começar com CARACTER ESPECIAL;
- Começar com letras, sem acento ou underline;
- Letras MAIUSCULAS e MINUSCULAS têm diferença no Python;
- ```type()``` -> Ver o tipo da variável.

Em Python se usa mais:
1. camelCase -> Classes;
2. Snake_case -> Variáveis, funções e métodos;

Boas práticas: [PEP 8](https://peps.python.org/pep-0008/);
- Curso relacionado que fiz: [Python - Boas Práticas]()

### 3. NUMBERS

- int -> 3
- float -> 3.1

Operations:

```python
1 + 1  -> Adição
1 - 1  -> Subtração
1 * 1  -> Multiplicação
1 / 1  -> Divisão
1 // 1 -> Divisão inteira

1 ** 2 -> Potência
1 % 1  -> Módulo
```
- Transformar um resultado float para int, só colocar o ```int()``` e colocar o resultado/variável, dentro dos parenteses.

### Texto

- string -> "Texto"

#### Formatação do Text

```python
thing = "World"
name = "Victor"
last_name = "Fedatto"

print("Hello,", thing) # Hello, World (print with space between)
print("Hello," + thing) # Hello,World (without blank space)
print("Hello," + thing, "of Victor") #Hello,World of Victor (without and with blank space)

#Mais usadas:
print("Hello, %s" % thing) #Para tratamento de dados, essa é a mais SEGURA. Porque ela transforma para String.

print("Hello, %s %s" % (name, last_name)) #you MUST have to put the () before and after the variables.

print(f"Hello, {thing}") #Mais agradável.

print("Hello, {} {}".format(name, last_name)) #A ordem importa aqui.
```

#### Métodos do Text
```python

name.upper() # VICTOR
name.lower() # victor

name[0] # 'V'
name.count("t") # 1
name.find("t") # 3 - index 3

name.encode() #Transform to bytes
name.encode().decode() #O resultado do "encode" vai ser usado para o "decode" para voltar ao normal a sua variável.

name.replace([target], [context])
name.replace("v", "b") # Bictor

phone = "(83) 98766-5432"
phone.replace("-", "").replace(")", "").replace("(", "") # 83 987665432

"-".join(name) #V-i-c-t-o-r

full_name = Victor H Fedatto
full_name.split(" ") # ['Victor', 'H', 'Fedatto']

#Tratamento de variáveis
name = "xVictorx"
name.strip("x") #Victor -> Só faz isso para caracteres no começo e no final.
name.rstrip("x") #xVictor -> Corta só o Right.

name.startswith("Vi")   #True
"tor" in full_name      #True
"tor" not in full_name  #False
```

- Uma variável não pode ser editada ou alterada. Você pode criar outra a partir dela, mas nunca editar.

### Booleans
- True // False
- Operadores Lógicos:

    - AND -> True and True
    - OR -> True or True | True or False
    - NOT -> Change

### Lists
- Coleção de elementos ordenáveis (index) e mutáveis (pode editar);
```python
orders = ["Apple", "Banana", "Orange", "Pizza", "Calzone"]

print(orders[0]) # Apple
print(orders[1:4]) # ["Banana", "Orange", "Pizza"]
print(orders[:4]) # ["Apple", "Banana", "Orange", "Pizza"]
print(orders[1:]) # ["Banana", "Orange", "Pizza", "Calzone"]

orders[0] = "Cake" # ["Cake", "Banana", "Orange", "Pizza", "Calzone"] 
```

#### Métodos:
```python
orders.append("Egg") # ["Cake", "Banana", "Orange", "Pizza", "Calzone", "Egg"]
orders.index("Egg") # 5
orders.insert(0, "Cereal") # ["Cereal", "Cake", "Banana", "Orange", "Pizza", "Calzone", "Egg"]

orders.pop(1) # ["Cereal", "Banana", "Orange", "Pizza", "Calzone", "Egg"]
orders.remove("Calzone") # ["Cereal", "Banana", "Orange", "Pizza", "Egg"]

orders.sort() # ['Banana', 'Cereal', 'Egg', 'Orange', 'Pizza']
```

### Tuplas

- Coleção ordenada e IMUTÁVEL (não pode mudar - remover, adicionar etc) de elementos.

```python
tupla = (1,1,2,3,4,5)

tupla[0] # 1
tupla[-1] # Ultimo elemento - 5
```

#### Métodos

```python
cont = tupla.count(1) # 2
index = tupla.index(0) # 1
```

### Dicionários
- Coleção não ordenada de pares chave-valor.

```python
dic = {
    "name": 'Victor',
    "last_name": 'Fedatto',
    "age": 21,
    "gender": 'male',
    "city": "Joao Pessoa",
    "watch_list": ["Hunger Games", "Star Wars VIII", "FNAF 2"]
}

print(dic)

#Acessar valores pela chave

print(f"Name: {dic["name"]}")
print(f"Age: {dic["age"]}")
print(f"Watch List: {dic["watch_list"]}")

# Adicionar
dic["favorite_color"] = "Crimson Violet"
dic["color_hex"] = "#4E132C"
```

#### Métodos

```python
# Excluir - chave:valor 
del dic["city"]
del dic["color_hex"]
del dic["favorite_color"]

# Retorno de chaves

chaves = dic.keys() # dict_keys(['name', 'last_name', 'age', 'gender', 'watch_list'])
chaves_list = list(dic.keys()) # ['name', 'last_name', 'age', 'gender', 'watch_list']
chaves_list[0] # 'name' -> Para acessar cada elemento individualmente.

# Retorno de todos os valores

values = dic.values() # dict_values(['Victor', 'Fedatto', 21, 'male', ['Hunger Games', 'Star Wars VIII', 'FNAF 2']])
values_list = list(dic.values()) # ['Victor', 'Fedatto', 21, 'male', ['Hunger Games', 'Star Wars VIII', 'FNAF 2']]
values_list[0] # Victor 

# Retornar lista de tuplas - cada elementos é uma tupla chave:valor

pares = dic.items() # dict_items([('name', 'Victor'), ('last_name', 'Fedatto'), ('age', 21), ('gender', 'male'), ('watch_list', ['Hunger Games', 'Star Wars VIII', 'FNAF 2']))
pares_list = list(dic.items()) # [('name', 'Victor'), ('last_name', 'Fedatto'), ('age', 21), ('gender', 'male'), ('watch_list', ['Hunger Games', 'Star Wars VIII', 'FNAF 2'])]
pares_list[0] # ('name', 'Victor')

print("Primeira chave-valor: %s = %s" % (pares_list[0][0], pares_list[0][1])) # name = Victor
```
---

We have finished this classes (01 to 15).
Next class: [Conditionals](conditionals.md)