#!/bin/bash

gnuplot

plot "tiempos2.csv" using 1:2 title 'Simple' with lines, \
     "tiempos2.csv" using 1:3 title 'Memoria' with lines