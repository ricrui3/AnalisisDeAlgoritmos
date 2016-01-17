def bfs(graph, start):
    path = []
    queue = [start]
    while queue:
        v = queue.pop(0)  # pops out the first in (go wider)
        if v not in path:
            path += [v]
            queue += graph[v]  # push v's neighbors to queue
    return path


def crear_matriz_dict_costos(Mc, Mg, n):
    auxG = set()
    auxC = []
    for i in range(n):
        strAux = input().split()
        for j in range(n):
            iaux = int(strAux[j])
            auxC.append(iaux)
            if iaux > 0:
                auxG.add(j)
        Mg[i] = auxG.copy()
        Mc.append(list(auxC[0: n]))
        auxC.clear()
        auxG.clear()
    return Mg


def costo(nodosV, matriz_costos):
    cost = 0
    for i in range(len(nodosV) - 1):
        cost += matriz_costos[nodosV[i]][nodosV[i + 1]]
    return cost


n = int(input())
matriz_grafo = {}
matriz_costos = []
crear_matriz_dict_costos(matriz_costos, matriz_grafo, n)
print(matriz_costos)
print(matriz_grafo)
nodoInicial = int(input())
nodoFinal = int(input())
nodosVisitados = bfs(matriz_grafo, nodoInicial)
print(nodosVisitados)
cost = costo(nodosVisitados, matriz_costos)
print("El costo de la primer ruta encontrada fue " + str(cost))
