class Graph:
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

    def display(self):
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))

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

class DirectedGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def insert_edge(self, from_vertex, to_vertex, weight=1):
        if 0 <= from_vertex < self.num_vertices and 0 <= to_vertex < self.num_vertices:
            self.adj_matrix[from_vertex][to_vertex] = weight

    def remove_edge(self, from_vertex, to_vertex):
        if 0 <= from_vertex < self.num_vertices and 0 <= to_vertex < self.num_vertices:
            self.adj_matrix[from_vertex][to_vertex] = 0

    def has_edge(self, from_vertex, to_vertex):
        if 0 <= from_vertex < self.num_vertices and 0 <= to_vertex < self.num_vertices:
            return self.adj_matrix[from_vertex][to_vertex] != 0
        return False

    def get_edge_weight(self, from_vertex, to_vertex):
        if 0 <= from_vertex < self.num_vertices and 0 <= to_vertex < self.num_vertices:
            return self.adj_matrix[from_vertex][to_vertex]
        return None

    def display(self):
        for row in self.adj_matrix:
            print(row)



# Começando a questão
'''8 - Questão - Considerando um sistema de transporte urbano, imagine uma cidade modelada como um grafo direcionado e ponderado com os tempo entre as estações, onde:
- Cada vértice representa um ponto de ônibus.
- Cada aresta direcionada entre dois vértices representa uma rota de ônibus direta entre os pontos.
- O peso da aresta representa o tempo, em minutos, que o ônibus leva para percorrer essa rota.
Considere o grafo a seguir, onde os vértices são identificados por letras e os pesos das arestas são indicados ao lado delas:
Responda as questões:

a) Represente o grafo acima.
b) Qual o tempo gasto para percorrer o caminho: {A-B-D}?
c) Quantas arestas tem no vértice B?
d) Qual a soma de todos os tempos encontrados na arestas A?
e) Quantas saídas e entradas tem o vértice B?
f) Encontre o caminho de menor tempo entre os vértices A até F.'''

grafo = [
    [0,5,2,0,5,0], #a
    [0,0,0,7,3,0], #b
    [0,0,0,2,0,0], #c
    [0,0,0,0,0,4], #d
    [0,0,0,0,0,2], #e
    [0,0,0,0,0,0], #f
]

grafo1 = DirectedGraph(len(grafo)) #len(grafo) retorna 6

for i in range(len(grafo)):
    for j in range(len(grafo)):
        if grafo[i][j] !=0:
            grafo1.insert_edge(i, j, grafo[i][j])

#a
grafo1.display()

#b - Tempo = Soma dos números
tempo = grafo1.get_edge_weight(0, 1) + grafo1.get_edge_weight(1, 3)
print(f"Tempo A-B-D: {tempo}")

#c - Contagem de arestas em um vértice
arestas_b = sum(1 for peso in grafo1.adj_matrix[1] if peso != 0)
print(f"Arestas saindo de B: {arestas_b}")

#d - soma de todos os tempos encontrados nas arestas A
soma_tempos_a = sum(grafo1.adj_matrix[0])
print(f"Soma dos tempos das arestas A: {soma_tempos_a}")

#e - Quantas saídas e entradas tem o vértice B
saidas_b = sum(1 for peso in grafo1.adj_matrix[1] if peso != 0)
entradas_b = sum(1 for i in range(6) if grafo1.adj_matrix[i][1] != 0)
print(f"Saídas de B: {saidas_b}, Entradas em B: {entradas_b}")


#f - Menor caminho entre A e F
#Professor não ensinou a fazer isso com código;