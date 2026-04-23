# ROCKETSEAT - PYTHON
Professor: Gabriel Casemiro

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

### Texto e Booleanos

- string -> "Texto"
- boolean -> True, False;

#### Formatação do Text
- 