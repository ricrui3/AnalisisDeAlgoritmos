__author__ = 'MrRubik'

import math


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
    n = input()
    fb = fibonacciTramposo(n)
    # print(fb)


inicio()
