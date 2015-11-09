# coding=utf-8
__author__ = 'MrRubik'


def fibonacciSimple(n):
    if n == 0 or n == 1:
        return n
    else:
        if (M[n - 1] == "E"):
            M[n - 1] = fibonacciSimple(n - 1)
        if (M[n - 2] == "E"):
            M[n - 1] = fibonacciSimple(n - 2)
        M[n] = M[n - 1] + M[n - 2]
        return M[n]


def inicio():
    print(M)
    print("tamanio de matriz es: " + len(M).__str__())
    n = input()
    for x in range(n - 1):
        M.append("E")
    fb = fibonacciSimple(n)
    print("el num fib " + n.__str__() + " es: " + fb.__str__())
    print(M)


M = [0, 1]
inicio()
