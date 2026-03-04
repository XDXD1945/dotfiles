#!/bin/bash

# Comprobar si mpstat está instalado
if ! command -v mpstat &> /dev/null; then
    echo "Error: 'mpstat' no está instalado. Instálalo con: sudo apt install sysstat"
    exit 1
fi

echo "--- Uso detallado por Hilo/Core ---"

# Ejecuta mpstat para todos los procesadores (-P ALL) 
# Captura una muestra durante 1 segundo, extrae las columnas de CPU e Idle
# Luego calcula el uso restando el idle a 100
mpstat -P ALL 1 1 | awk '/^[0-9]/ && $3 != "all" {
    usage = 100 - $NF;
    printf "Core %s: %.3f%%\n", $3, usage
}'
