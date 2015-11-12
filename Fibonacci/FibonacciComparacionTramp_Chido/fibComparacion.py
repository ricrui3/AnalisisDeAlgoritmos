__author__ = 'mrubik'

import math


def mult_matrices(matriz, matriz1):
    aux = [[0, 0], [0, 0]]
    aux[0][0] = matriz[0][0] * matriz1[0][0] + matriz[0][1] * matriz1[1][0]
    aux[0][1] = matriz[0][0] * matriz1[0][1] + matriz[0][1] * matriz1[1][1]
    aux[1][0] = matriz[1][0] * matriz1[0][0] + matriz[1][1] * matriz1[1][0]
    aux[1][1] = matriz[1][0] * matriz1[0][1] + matriz[1][1] * matriz1[1][1]
    return aux


def mipowMat(matriz, n):
    if n == 0:
        matriz = [[1, 0], [0, 1]]
        return matriz
    if n == 1:
        return matriz
    if n > 1:
        if n % 2 == 0:
            t = mipowMat(matriz, n / 2)
            return mult_matrices(t, t)
        else:
            t = mipowMat(matriz, (n - 1) / 2)
            return mult_matrices(mult_matrices(t, t), matriz)


def fibonacci_chido(n):
    matriz = [[1, 1], [1, 0]]
    aux = mipowMat(matriz, n)
    return aux[0][1]


def mipow(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    if n > 1:
        if n % 2 == 0:
            t = mipow(a, n / 2)
            return t * t
        else:
            t = mipow(a, (n - 1) / 2)
            return t * t * a


def fibonacciTramposo(n):
    phi = (1 + math.sqrt(5)) / 2
    t = mipow(phi, n)
    return t / math.sqrt(5)


def inicio():
    # n = input()
    pot_dos = 10
    for x in range(pot_dos):
        fbT = fibonacciTramposo(mipow(2, x))
        fbC = fibonacci_chido(mipow(2, x))
        aux = fbC - fbT
        print(mipow(2, x).__str__() + "    " + fbT.__str__() + "      " + fbC.__str__() + "     " + aux.__str__())


inicio()
