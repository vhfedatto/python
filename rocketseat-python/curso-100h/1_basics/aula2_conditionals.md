# ROCKETSEAT - PYTHON

Professor: Gabriel Casemiro Rocketseat
Aluno: Victor H Fedatto Vasconcelos

```OBS: Alguns conceitos básicos da linguagem eu não vou focar tanto, pois eu já sou intermediário em Python (e estou fazendo o curso do 0 até o avançado).```

## Conditionals (Lesson 16th)

```python
age = 20

if age >= 18:
    print("You are over 18")

elif age <= 18:
    print("You are underage")

else: 
    print("You have to type a valid number.")

#Outro jeito de usar if e else

msg = "You can get a driver's license in Brazil." if age >= 18 else "YOu can't get a driver's license in Brazil"
```

## Input

```python
age = int(input("How old are you?"))

print(f"You are {age} years old")
```

## Loops
```python
lista = [1,2,3,4,5]

for i in lista:
    print(i) # 1 2 3 4 5

dic = {"name": "Victor", "age": 20, "college": "UNIESP"}
print("Using dictionary - keys")

for key in dic.keys():
    print(key)

for value in dic.value():
    print(value)

for key, value in dic.items():
    print(f"{key}: {value}")

# Other things about for
for i in range(5):
    print("Number:", i)

lista2 = [1,2,3,4,5]

for i in range(0, len(lista2)):
    print(f"Index: {i}")
    print(f"Element: {lista2[index]}")

lis_enum = ["a", "b", "c"]

for i, j in enumerate(lis_enum):
    print(f"{i}: {j}")
```

- Enumerate() -> index & value

## While

```python
c = 0

while c < 5:
    print("Value:", c)
    c += 1
```

## Functions

- bloco de código que executa uma função toda vez que ele é chamado.

```python
def hello (name):
    print("Hello, %s!" % name)

print("Welcome!")

hellO("Alice")
hellO("Victor")

def soma(n1, n2):
    result = n1 + n2
    return result

n1 = 20
n2 = 50

resultado_soma = soma(n1, n2)
print(f"O resultado da soma de {n1} e {n2} é {resultado_soma}")
```

## EXCEPTIONS

- Bloco de código que ele tente. Se não der certo, vai para a exceção.
- try, except, raise, else e finally.

```python
try:
    num = int(input("Type a number: "))
    res = 10/num

except ValueError as e:
    print(f"Error of value error: {e}")
    raise ValueError("Tipo de variáveis incompativeis")

except Exception as e:
    print(f"Error: {e}")

else: # Executa caso seja bem sucedido.
    print(f"Result: {res}")

finally: # Executar mesmo com exceção - vai fazer de toda forma
    print("Operação Finalizada")
```

---
We have finished this classes (16 to 30).
Next class: [OOP](aula3_poo.md)