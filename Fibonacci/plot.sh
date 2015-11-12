#!/bin/bash

gnuplot

plot "tiempos.csv" using 1:2 title 'Simple' with lines, \
     "tiempos.csv" using 1:3 title 'Memoria' with lines, \
     "tiempos.csv" using 1:4 title 'Iterativo' with lines,\
     "tiempos.csv" using 1:5 title 'Tramposo' with lines, \
     "tiempos.csv" using 1:6 title 'Chido' with lines