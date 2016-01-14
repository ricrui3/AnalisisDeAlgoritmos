__author__ = 'mrubik'


def bp(grafo, nodoI):
    nodosVisitados = set()
    pila = [nodoI]
    while pila:
        nodo = pila.pop()
        if nodo not in nodosVisitados:
            nodosVisitados.add(nodo)
            pila.extend(grafo[nodo] - nodosVisitados)
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
print(bp(matriz_grafo, nodoInicial))
