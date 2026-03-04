#!/bin/bash

# Obtenemos los datos en Megabytes para mayor precisión decimal
read total usada <<< $(free -m | awk 'NR==2 {print $2, $3}')

# Convertimos MB a GB con un decimal usando 'bc' o 'awk'
# Usamos awk para la operación matemática de forma limpia
awk -v t="$total" -v u="$usada" 'BEGIN {
    printf "%.1fG/%.0fG\n", u/1024, t/1024
}'
