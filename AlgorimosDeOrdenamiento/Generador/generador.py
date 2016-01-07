#!/usr/bin/python
import random


# Donde:
#	n = cantidad de numeros a generar
#	li = primer numero posible a generar
#   ls = ultimo numero posible a generar 
def generador(n, li, ls):
	print(n)
	for x in range(1, n + 1):
		rI = random.randint(li, ls)
		print(rI)
	pass


n = input()
li = input()
ls = input()
generador(n, li, ls)
