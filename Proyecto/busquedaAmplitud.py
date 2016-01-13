 def bfs(graph, start):
    nodosVisitados, cola = set(), [start]
    while cola:
        nodo = cola.pop(0)
        if nodo not in nodosVisitados:
            nodosVisitados.add(nodo)
            cola.extend(graph[nodo] - nodosVisitados)
    return nodosVisitados

def crear_matriz_dict(M, n):
    aux = set()
    for i in range(n):
        strAux = input().split()
        for j in range(n):
            iaux = int(strAux[j])
            if iaux > 0:
                aux.add(j)
        M[i] = aux.copy()
        aux.clear()
    return M


n = int(input())
matriz_grafo = {}
crear_matriz_dict(matriz_grafo, n)
nodoInicial = int(input())
print(bfs(matriz_grafo, nodoInicial))