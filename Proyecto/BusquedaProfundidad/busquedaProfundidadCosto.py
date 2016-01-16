__author__ = 'mrubik'


def bp(grafo, nodoI, nodoF):
    nodosVisitadosD = set()
    nodosVisitadosL = []
    pila = [nodoI]
    pilaAux = [[nodoI]]
    indice = 0
    nodo = pila.pop()
    dictToList = []
    while nodo != nodoF:
        if len(pilaAux[indice]) == 0:
            nodosVisitadosL.pop()
            indice -= 1
        if nodo not in nodosVisitadosD:
            nodosVisitadosD.add(nodo)
            nodosVisitadosL.append(nodo)
            nodosPorVisitar = grafo[nodo] - nodosVisitadosD
            indice += 1
            dictToList.extend(nodosPorVisitar)
            pilaAux.append(list(dictToList[0:len(dictToList)]))
            dictToList.clear()
            pila.extend(nodosPorVisitar)
        nodo = pila.pop()
        pilaAux[indice].pop()
    nodosVisitadosL.append(nodoF)
    return nodosVisitadosL


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
nodosVisitados = bp(matriz_grafo, nodoInicial, nodoFinal)
print(nodosVisitados)
cost = costo(nodosVisitados, matriz_costos)
print("El costo de la primer ruta encontrada fue " + str(cost))
