__author__ = 'mrubik'

import sys
from random import randint

#Para modificar los posibles caracteres a mostrarse
#en las cadenas agregar o quitar valores de "posibilidadesCadena"
posibilidadesCadena = ["A", "B", "C"]
tam = len(posibilidadesCadena) - 1


def imprimir_cadena(tamanio):
    for i in range(tamanio):
        valor = randint(0, tam)
        print("'"+posibilidadesCadena[valor]+"'")


def inicio():
    n = sys.argv[1]
    n = int(n)

    #Tamanio de las dos cadenas
    print(2*n)

    #"Primer Cadena"
    imprimir_cadena(n)

    #Segunda Cadena
    imprimir_cadena(n)

inicio()