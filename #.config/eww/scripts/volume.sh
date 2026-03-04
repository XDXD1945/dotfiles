#!/bin/bash

# Obtener el volumen del sink predeterminado
volumen=$(pactl get-sink-volume @DEFAULT_SINK@ | grep -Po '[0-9]+(?=%)' | head -n 1)

# Imprimir solo el número con el símbolo de porcentaje
echo "${volumen}%"
