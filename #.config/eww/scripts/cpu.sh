#!/bin/bash

# Leer la primera captura de estadísticas de la CPU
read -r _ user nice system idle iowait irq softirq steal _ < /proc/stat
prev_idle=$((idle + iowait))
prev_total=$((user + nice + system + idle + iowait + irq + softirq + steal))

# Esperar un segundo para calcular la diferencia
sleep 1

# Leer la segunda captura
read -r _ user nice system idle iowait irq softirq steal _ < /proc/stat
now_idle=$((idle + iowait))
now_total=$((user + nice + system + idle + iowait + irq + softirq + steal))

# Calcular la diferencia entre capturas
diff_idle=$((now_idle - prev_idle))
diff_total=$((now_total - prev_total))

# Calcular el porcentaje de uso
# Se usa (1000 * ...) / diff_total para obtener un decimal con bc o awk
usage=$(awk "BEGIN {printf \"%.1f\", 100 * ($diff_total - $diff_idle) / $diff_total}")

echo "${usage}%"
