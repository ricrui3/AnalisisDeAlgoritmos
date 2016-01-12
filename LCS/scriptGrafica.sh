#!/bin/bash

#maximo tamaño dos a la "k" a multiplicar
k=21

#primer linea a imprimir
echo "tamaño        lcs_rec        lcs_iter"

for (( i = 0; i < "$k"; i++ )); do
	valor_n=$(python -c "print 2 ** $i")
	# Inicio de cada uno de los programas de multiplicacion de matrices para el valor "valor_n"

	#tiempo1=$((/usr/bin/time -f "%U" python lcs.py < cadenas/$valor_n.txt) 2>&1)
	tiempo2=$((/usr/bin/time -f "%U" python lcs_iterativo.py < cadenas/$valor_n.txt) 2>&1)

	echo "$valor_n        x.xx        $tiempo2"

done
