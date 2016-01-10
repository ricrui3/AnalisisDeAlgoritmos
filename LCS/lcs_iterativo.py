def lcs_iterativo(x, y, i, j):
    for p in range(1, i + 2):
        for q in range(1, j + 2):
            lcs = matriz_LCS
            flechas = matriz_flechas
            if x[p - 1] == y[q - 1]:
                matriz_LCS[p][q] = matriz_LCS[p - 1][q - 1] + 1
                matriz_flechas[p - 1][q - 1] = 0
            else:
                if matriz_LCS[p - 1][q] >= matriz_LCS[p][q - 1]:
                    matriz_LCS[p][q] = matriz_LCS[p - 1][q]
                    matriz_flechas[p - 1][q - 1] = 2
                else:
                    matriz_LCS[p][q] = matriz_LCS[p][q - 1]
                    matriz_flechas[p - 1][q - 1] = 1


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


def creacion_cadena(A, n):
    for i in range(0, n):
        aux = str(input())
        A.append(aux)
    return A


def crear_matriz(n, num):
    M = []
    for i in range(n):
        M.append([num] * n)
    return M


def renglon_columna_ceros(i, j, matriz):
    for z in range(i + 2):
        matriz[z][0] = 0
    for z in range(j + 2):
        matriz[0][z] = 0


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
matriz_LCS = crear_matriz(n + 1, -1)
renglon_columna_ceros(i, j, matriz_LCS)
matriz_flechas = crear_matriz(n, -1)
creacion_cadena(x, n)
creacion_cadena(y, n)
pila_LCS = []
pila_LCS_final = []

lcs_iterativo(x, y, i, j)
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
