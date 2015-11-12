#!/bin/bash

#maximo tamaño dos a la "k" a multiplicar
k=15

#primer linea a imprimir
echo "tamaño        Simple        Memoria        Iterativo        Tramposo        Chido"

for (( i = 0; i < "$k"; i++ )); do
	valor_n=$(python -c "print 2 ** $i")
	# Inicio de cada uno de los programas de multiplicacion de matrices para el valor "valor_n"

	tiempo1=$((/usr/bin/time -f "%U" python FibonacciSimple/fibonacciSimple.py < TamaniosMatrices/$valor_n.txt) 2>&1)
	tiempo2=$((/usr/bin/time -f "%U" python FibonacciConMemoria/fibonnacciConMemoria.py < TamaniosMatrices/$valor_n.txt) 2>&1)
	tiempo3=$((/usr/bin/time -f "%U" python FibonacciIterativo/fibonacciIterativo.py < TamaniosMatrices/$valor_n.txt) 2>&1)
	tiempo4=$((/usr/bin/time -f "%U" python FibonacciTramposo/fobonacciTramposo.py < TamaniosMatrices/$valor_n.txt) 2>&1)
	tiempo5=$((/usr/bin/time -f "%U" python FibonacciChido/fibonacciChido.py < TamaniosMatrices/$valor_n.txt) 2>&1)

	echo "$valor_n        $tiempo1        $tiempo2        $tiempo3        $tiempo4        $tiempo5"

done
