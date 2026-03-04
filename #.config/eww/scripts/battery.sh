#!/bin/bash

# Buscamos la batería principal (usualmente BAT0 o BAT1)
BAT=$(ls /sys/class/power_supply/ | grep BAT | head -n 1)

if [ -z "$BAT" ]; then
    echo "No se detectó batería"
    exit 1
fi

# Leemos la capacidad actual
CAPACITY=$(cat /sys/class/power_supply/$BAT/capacity)

echo "${CAPACITY}%"
