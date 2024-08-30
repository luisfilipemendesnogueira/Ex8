import heapq

def prim_mst(graph):
    num_vertices = len(graph)
    visitado = [False] * num_vertices
    mst = []
    min_heap = [(0, 0, -1)]  # (custo, nó atual, nó pai)

    while min_heap:
        custo, u, pai = heapq.heappop(min_heap)
        if visitado[u]:
            continue

        visitado[u] = True
        if pai != -1:
            mst.append((pai, u, custo))

        for v, peso in graph[u]:
            if not visitado[v]:
                heapq.heappush(min_heap, (peso, v, u))

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

mst = prim_mst(graph)
print("Árvore Geradora Mínima (Prim):")
for u, v, peso in mst:
    print(f"{u} -- {v} == {peso}")
