#!/bin/bash

#primer linea a imprimir
echo ""
echo "Nodos visitados con el algoritmo de busqueda en profundidad con el archivo prueba1.in"
tiempo4=$((/usr/bin/time -f "tiempo %e" python3.4 busquedaProfundidad.py < archivosProfesor/prueba1.in) 2>&1)
echo "$tiempo4"

echo ""
#segunda linea a imprimir
echo "Nodos visitados con el algoritmo de busqueda en profundidad con el archivo prueba2.in"
tiempo5=$((/usr/bin/time -f "tiempo %e" python3.4 busquedaProfundidad.py < archivosProfesor/prueba2.in) 2>&1)
echo "$tiempo5"

echo ""
#tercera linea a imprimir
echo "Nodos visitados con el algoritmo de busqueda en profundidad con el archivo prueba3.in"
tiempo6=$((/usr/bin/time -f "tiempo %e" python3.4 busquedaProfundidad.py < archivosProfesor/prueba3.in) 2>&1)
echo "$tiempo6"
