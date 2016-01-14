def dijkstra(G, Ma, s):
    n = len(G)
    vDdelta = crearVectorF(n)
    vPi = crearVectorI(n)

    if int(s) not in G:
        print("Error, no se encontro el nodo en G")
        return -1

    vDdelta[posicion(G, s)] = 0
    Q = crearVectorI(n)
    V = list(G[0: n])

    # print(V)

    while lenV >= 0:

        u = menor(V, vDdelta)  # devuelve el ID
        mover(u, V, Q)
        renglon = posicion(G, u)
        for i in range(0, n):
            if Ma[renglon][i] != None and Ma[renglon][i] != float('inf') and Ma[renglon][i] != 0:
                relajar(renglon, i, vDdelta, vPi, Ma)

    return vDdelta, vPi


def crearVectorF(n):
    F = []
    for x in range(0, n):
        F.append(float('inf'))
    return F


def crearVectorI(n):
    I = []
    for x in range(0, n):
        I.append(None)
    return I


def posicion(nodos, nodo):
    for i in nodos:
        if nodos[i] == nodo:
            return i
    return -1


def relajar(s, d, delta, pi, Ma):
    if (delta[d] > (delta[s] + Ma[s][d])):
        delta[d] = delta[s] + Ma[s][d]
        pi[d] = s
        return
    else:
        return


def mover(u, V, Q):
    global lenV
    V[u] = None
    Q[u] = u
    lenV -= 1
    return


def menor(V, delta):
    minim = float("inf")
    minimPos = 0
    for i in range(len(delta)):
        if V[i] is not None:  # significa que el nodo todavia esta en el vector v
            if delta[i] < minim:
                minim = delta[i]
                minimPos = i
    return minimPos


def crearMatriz(M, n):
    aux = []
    for i in range(n):
        strAux = input().split()
        for j in range(n):
            iaux = int(strAux[j])
            if iaux == -1:
                aux.append(float("inf"))
            else:
                aux.append(iaux)
        M.append(list(aux[0: n]))
        aux.clear()
    return M


def nombres_nodos(G, n):
    for x in range(0, n):
        G.append(x)


# G es el nombre de los nodos
# n es el tamanio de la matriz


G = []
Ma = []
n = int(input())
lenV = n

nombres_nodos(G, n)
crearMatriz(Ma, n)

s = int(input())

delta, pi = dijkstra(G, Ma, s)
print("\nvector delta")
print(delta)
print("vector pi")
print(pi)