class GraphPonderado:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        # Inicializa a matriz de adjacência com zeros
        self.adj_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def insert_edge(self, v1, v2, weight=1):
        if 0 <= v1 < self.num_vertices and 0 <= v2 < self.num_vertices:
            self.adj_matrix[v1][v2] = weight
            self.adj_matrix[v2][v1] = weight  # Para grafos não direcionados
        else:
            print(f"Erro: vértices {v1} e/ou {v2} fora do intervalo permitido.")

    def remove_edge(self, v1, v2):
        if 0 <= v1 < self.num_vertices and 0 <= v2 < self.num_vertices:
            self.adj_matrix[v1][v2] = 0
            self.adj_matrix[v2][v1] = 0  # Para grafos não direcionados
        else:
            print(f"Erro: vértices {v1} e/ou {v2} fora do intervalo permitido.")

    def has_edge(self, v1, v2):
        if 0 <= v1 < self.num_vertices and 0 <= v2 < self.num_vertices:
            return self.adj_matrix[v1][v2] != 0
        else:
            print(f"Erro: vértices {v1} e/ou {v2} fora do intervalo permitido.")
            return False

    def get_edge_weight(self, v1, v2):
        if 0 <= v1 < self.num_vertices and 0 <= v2 < self.num_vertices:
            return self.adj_matrix[v1][v2]
        else:
            print(f"Erro: vértices {v1} e/ou {v2} fora do intervalo permitido.")
            return None

    def display(self):
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))


#Começando a aplicação

dados = [
    [0,2,0,0,5,0], #a
    [2,0,3,0,0,0], #b
    [0,3,0,9,8,3], #c
    [0,0,9,0,0,0], #d
    [5,0,8,0,0,4], #e
    [0,0,3,0,4,0], #f
]

grafo = GraphPonderado(len(dados))

for i in range(len(dados)):
    for j in range(len(dados)):
        if dados[i][j] != 0:
            grafo.insert_edge(i, j, dados[i][j])

#a - apresentar o grafo
grafo.display()

#b - soma
soma_total = sum(sum(linha) for linha in grafo.adj_matrix) // 2
print("b) A soma total dos pesos das arestas: ", soma_total)

#c - quantas arestas tem peso com valor maior que 6
c = 0

for i in range(len(dados)):
    for j in range(i+1, len(dados)):
        if grafo.get_edge_weight(i,j) > 6:
            c+=1
print("c) Arestas com peso > 6: ", c)

#d - Qual é a aresta de menor valor
menor = float('inf')
for i in range(len(dados)):
    for j in range(len(dados)):
        peso = grafo.get_edge_weight(i, j)
        if 0 < peso < menor:
            menor = peso

print("d) Aresta de menor valor: ", menor)

#e - Qual a aresta de maior valor
maior = 0
for i in range(len(dados)):
    for j in range(len(dados)):
        peso = grafo.get_edge_weight(i, j)
        if peso > maior:
            maior = peso

print("e) Aresta de maior valor: ", maior)

#f - Qual é o caminho de menor custo entre os vértices A --> F
#g - Qual é caminho de maior custo entre os vértices A --> F

# professor não ensinou a fazer por código. Mas a resposta seria ABCF e ABCEF
from itertools import permutations

def custo_caminho(caminho):
    custo = 0
    for i in range(len(caminho) - 1):
        peso = grafo.get_edge_weight(caminho[i], caminho[i+1])
        if peso == 0:
            return float('inf')  # não existe conexão
        custo += peso
    return custo

# Caminhos possíveis curtos entre 0 (A) e 5 (F)
possiveis = [
    [0, 4, 5],          # A-E-F
    [0, 1, 2, 5],       # A-B-C-F
    [0, 1, 2, 4, 5],    # A-B-C-E-F
    [0, 4, 2, 5],       # A-E-C-F
    [0, 4, 2, 3, 5],    # A-E-C-D-F (D-F não existe)
]

validos = [(p, custo_caminho(p)) for p in possiveis if custo_caminho(p) != float('inf')]
melhor = min(validos, key=lambda x: x[1])
pior = max(validos, key=lambda x: x[1])

def formatar(caminho):
    return " -> ".join("ABCDEF"[v] for v in caminho)

print(f"f) Menor caminho: {formatar(melhor[0])} com custo {melhor[1]}")
print(f"g) Maior caminho: {formatar(pior[0])} com custo {pior[1]}")

#h - Qual é o grau do vértice C
grau_c = sum(1 for peso in grafo.adj_matrix[2] if peso !=0)
print("h) Grau do vértice C: ", grau_c)

#i - Qual é a soma das arestas adjacentes ao vértice C
soma_c = sum(grafo.adj_matrix[2])
print("i) Soma dos pesos das arestas de C: ", soma_c)

#j - Quais os vértices conectados ao nó C
conectados = [i for i, peso in enumerate(grafo.adj_matrix[2]) if peso != 0]
nomes = ["ABCDEF"[i] for i in conectados]
print("j) Vértices conectados a C:", ", ".join(nomes))