def bp(s):
    for i in matriz_adj[s]:
        if parent.index(matriz_adj[s][i]) is ValueError:
            parent.append(matriz_adj[s][i])


def bp_visita():
    return 0


# why is it not showing?

def recibir_grafo():
    return 0


def crearMatriz(n):
    M = []
    aux = []
    for i in range(n):
        strAux = input().split()
        for j in range(n):
            aux.append(int(strAux[j]))
        M.append(list(aux[0: n]))
        aux.clear()
    return M


n = int(input())
nom_nodos = ['A', 'B', 'C', 'D', 'E']
matriz_adj = crearMatriz(n)
parent = []

for i in range(n):
    print(matriz_adj[i])
