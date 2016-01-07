def mayor(param, param1):
    if param >= param1:
        return param
    elif param1 > param:
        return param1

print("camios")

def lcs(x, y, i, j):
    if i >= 0 and j >= 0:
        if matriz_LCS[i][j] != "E":
            return matriz_LCS[i][j]
        else:
            if x[i] == y[j]:
                aux = lcs(x, y, i - 1, j - 1)
                matriz_LCS[i][j] = aux + 1
                return matriz_LCS[i][j]
            else:
                matriz_LCS[i][j] = mayor(lcs(x, y, i - 1, j), lcs(x, y, i, j - 1))
                return matriz_LCS[i][j]
    return 0


def creacion_cadena(A, n):
    for i in range(0, n):
        aux = str(input())
        A.append(aux)
    return A


def crearMatriz(n, num):
    M = []
    for i in range(n):
        M.append([num] * n)
    return M


n = int(input())
n = int(n / 2)
x = []
y = []
i = n - 1
j = n - 1
creacion_cadena(x, n)
creacion_cadena(y, n)
matriz_LCS = crearMatriz(n, "E")
lcs(x, y, i, j)
print(x)
print(y)
print(" ")
for i in range(n):
    print(matriz_LCS[i])
