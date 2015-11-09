__author__ = 'mrubik'


def mult_matrices(matriz, matriz1):
    aux = [[0, 0], [0, 0]]
    aux[0][0] = matriz[0][0] * matriz1[0][0] + matriz[0][1] * matriz1[1][0]
    aux[0][1] = matriz[0][0] * matriz1[0][1] + matriz[0][1] * matriz1[1][1]
    aux[1][0] = matriz[1][0] * matriz1[0][0] + matriz[1][1] * matriz1[1][0]
    aux[1][1] = matriz[1][0] * matriz1[0][1] + matriz[1][1] * matriz1[1][1]
    return aux


def mipow(matriz, n):
    if n == 0:
        matriz = [[1, 0], [0, 1]]
        return matriz
    if n == 1:
        return matriz
    if n > 1:
        if n % 2 == 0:
            t = mipow(matriz, n / 2)
            return mult_matrices(t, t)
        else:
            t = mipow(matriz, (n - 1) / 2)
            return mult_matrices(mult_matrices(t, t), matriz)


def fibonacci_chido(n):
    matriz = [[1, 1], [1, 0]]
    aux = mipow(matriz, n)
    return aux[0][1]


def inicio():
    n = input()
    fb = fibonacci_chido(n)
    print(fb)


inicio()
