#!/bin/bash

#numero de archivos de 2 elevado a la n
n=50

for (( i = 0; i < "$n"; i++ )); do
		valor_n=$(python -c "print 2 ** $i")
		python tamanio.py ${valor_n} > ${valor_n}.txt
		echo "$valor_n"
done