class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        raiz_u = self.find(u)
        raiz_v = self.find(v)
        if raiz_u != raiz_v:
            if self.rank[raiz_u] > self.rank[raiz_v]:
                self.parent[raiz_v] = raiz_u
            elif self.rank[raiz_u] < self.rank[raiz_v]:
                self.parent[raiz_u] = raiz_v
            else:
                self.parent[raiz_v] = raiz_u
                self.rank[raiz_u] += 1

def kruskal_mst(graph):
    num_vertices = len(graph)
    edges = []
    for u in range(num_vertices):
        for v, peso in graph[u]:
            edges.append((peso, u, v))

    edges.sort()
    disjoint_set = DisjointSet(num_vertices)
    mst = []

    for peso, u, v in edges:
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst.append((u, v, peso))

    return mst

# Grafo representado como lista de adjacência
graph = {
    0: [(1, 6), (5, 8)],
    1: [(0, 6), (2, 6), (3, 7), (6, 3)],
    2: [(1, 6), (3, 8), (7, 3)],
    3: [(1, 7), (2, 8), (4, 5), (7, 2), (8, 4)],
    4: [(3, 5), (9, 2)],
    5: [(0, 8), (6, 9)],
    6: [(1, 3), (5, 9), (7, 4)],
    7: [(2, 3), (3, 2), (6, 4), (8, 6)],
    8: [(3, 4), (7, 6), (9, 3)],
    9: [(4, 2), (8, 3)]
}

mst = kruskal_mst(graph)
print("Árvore Geradora Mínima (Kruskal):")
for u, v, peso in mst:
    print(f"{u} -- {v} == {peso}")
