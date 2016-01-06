def lcs(x, y, i, j):
    if i > 0 and j > 0:
        if C[i, j] is not None:
            print "oh oh !"


def creacionArreglo(A, n):
    for i in range(0, n):
        x = input()
        A.append(x)
    return A

def crearMatriz(n, num):
    M = []
    for i in range(n):
        M.append([num] * n)
    return M

C=crearMatriz(2,0)
A = []
n = input()
creacionArreglo(A, n)
print(A)
