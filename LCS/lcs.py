def lcs(x, y, i, j):
    if i >= 0 and j >= 0:
        if matriz_LCS[i][j] != "E":
            return matriz_LCS[i][j]
        else:
            if x[i] == y[j]:
                matriz_LCS[i][j] = lcs(x, y, i - 1, j - 1) + 1
                matriz_flechas[i][j] = 0
                return matriz_LCS[i][j]
            else:
                mayor_flechas = mayor(lcs(x, y, i - 1, j), lcs(x, y, i, j - 1))
                matriz_LCS[i][j] = mayor_flechas[0]
                matriz_flechas[i][j] = mayor_flechas[1]
                return matriz_LCS[i][j]
    return 0


def cadena_final_lcs():
    i = j = n - 1
    while i >= 0 and j >= 0:
        if matriz_flechas[i][j] == 0:
            pila_LCS.append(x[i])
            i -= 1
            j -= 1
        elif matriz_flechas[i][j] == 1:
            j -= 1
        elif matriz_flechas[i][j] == 2:
            i -= 1


def mayor(param, param1):
    if param >= param1:
        return [param, 2]
    elif param1 > param:
        return [param1, 1]


def creacion_cadena(A, n):
    for i in range(0, n):
        aux = str(input())
        A.append(aux)


def crearMatriz(M, n, num):
    for i in range(n):
        M.append([num] * n)
    return M


# ---

# n es el tamanio de la cadena
# x es la primer cadena
# y es la segunda cadena
# j e i son el tamanio de la cadena 'x' y 'y' respectivamente
# matriz_LCS es donde se guarda la matriz de valores
# matriz_flechas es donde se guardan las felchas correspondientes para conseguir la cadena
#   0 significa diagonal
#   1 significa izquierda
#   2 significa arriba

n = int(input())
n = int(n / 2)
x = []
y = []
i = n - 1
j = n - 1
matriz_LCS = []
crearMatriz(matriz_LCS, n, "E")
matriz_flechas = []
crearMatriz(matriz_flechas, n, "E")
creacion_cadena(x, n)
creacion_cadena(y, n)
pila_LCS = []
pila_LCS_final = []


lcs(x, y, i, j)
cadena_final_lcs()

print(x)
print(y)

print("\n")
for i in range(n):
    print(matriz_LCS[i])

print("\n")
for i in range(n):
    print(matriz_flechas[i])

print("\n")

for i in range(len(pila_LCS)):
    pila_LCS_final.append(pila_LCS.pop())

print(pila_LCS_final)
