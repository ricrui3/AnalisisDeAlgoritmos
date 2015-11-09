#!/usr/bin/env bash

#maximo tamaño dos a la "k" a multiplicar
k=15

#primer linea a imprimir
echo "tamaño        Ingenua        Recursiva"

for (( i = 1; i < "$k"; i++ )); do
	valor_n=$(python -c "print 2 ** $i")
	# Inicio de cada uno de los programas de multiplicacion de matrices para el valor "valor_n"

	tiempo1=$((/usr/bin/time -f "%U" python ../multiplicacionIngenua/multiplicacionIngenua.py < ../TamaniosMatrices/$valor_n.txt) 2>&1)
	tiempo2=$((/usr/bin/time -f "%U" python ../MultiplicacionRecursiva/multiplicacionRecursiva.py < ../TamaniosMatrices/$valor_n.txt) 2>&1)
	#tiempo3=$((/usr/bin/time -f "%U" python ../MultiplicacionDeStrassen/multiplicacionDeStrassen.py < ../TamaniosMatrices/$valor_n.txt) 2>&1)

	echo "$valor_n        $tiempo1        $tiempo2"

done