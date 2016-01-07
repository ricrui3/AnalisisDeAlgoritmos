def mayor(param, param1):
    if param > param1:
        return param
    elif param1 > param:
        return param1


def lcs(x, y, i, j):
    if i > 0 and j > 0:
        if matriz_LCS[i][j] is not None:
            if x[i] == y[j]:
                matriz_LCS[i][j] = lcs(x,y,i-1,j-1) + 1
            else:
                matriz_LCS[i][j] = mayor(lcs(x,y,i-1,j),lcs(x,y,i,j-1))



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
n = int(n/2)
x = []
y = []
i = n
j = n
creacion_cadena(x, n)
creacion_cadena(y, n)
matriz_LCS = crearMatriz(n, None)
lcs(x,y,i,j)
print(x)
print(y)
print(matriz_LCS)
