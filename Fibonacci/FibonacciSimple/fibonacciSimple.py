__author__ = 'MrRubik'

M = [0, 1]


def fibonacciSimple(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacciSimple(n - 1) + fibonacciSimple(n - 2)


def inicio():
    n = input()
    fb = fibonacciSimple(n)
    print(fb)


inicio()
