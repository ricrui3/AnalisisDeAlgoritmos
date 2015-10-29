__author__ = 'MrRubik'

def fibonacciIterativo(n):
    if n == 0 or n == 1:
        return n
    else:
        a = 0L
        b = 1L
        for x in range(n-1):
            c = a + b
            a = b
            b = c
        return c

def inicio():
    n = input()
    fb = fibonacciIterativo(n)
    print(fb)

inicio()