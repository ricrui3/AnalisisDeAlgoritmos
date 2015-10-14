# coding=utf-8
__author__ = 'Ricardo Ruiz Maldonado'
import random


def quickSort(A, n):
    qsr(A, 0, n - 1)
    return A


def qsr(A, p, q):
    # A = Arreglo de numeros
    # p = Primera posición del arreglo
    #
    if q > p:
        r = partir(A, p, q)
        qsr(A, p, r - 1)
        qsr(A, r + 1, q)
    return A


def partir(A, p, q):
    a = random.randint(p + 1, q)
    intercambiar(A, p, a)
    pivote = A[p]
    i = p
    for j in range(i + 1, q + 1):
        if A[j] <= pivote:
            i = i + 1
            intercambiar(A, i, j)
    intercambiar(A, p, i)
    return i


def intercambiar(A, i, j):
    aux = A[i]
    A[i] = A[j]
    A[j] = aux


def creacionArreglo(A, n):
    for i in range(0, n):
        x = input()
        A.append(x)
    return A


# A = [10,88,13,15,6]
# n = 5
A = []
n = input()
creacionArreglo(A, n)
quickSort(A, n)
print(A)
