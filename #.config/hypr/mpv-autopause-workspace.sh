#!/bin/bash

SOCKET="/tmp/mpvpaper.sock"

while true; do
    # Workspace activo
    ACTIVE_WS=$(hyprctl -j activeworkspace | jq '.id')

    # Ventanas visibles en workspace actual EXCEPTO kitty
    WINDOW_COUNT=$(hyprctl -j clients | jq "[.[] 
        | select(
            .workspace.id == $ACTIVE_WS 
            and .mapped == true 
            and .class != \"kitty\"
        )
    ] | length")

    if [ "$WINDOW_COUNT" -gt 0 ]; then
        # Pausar si hay ventanas que NO sean kitty
        echo '{ "command": ["set_property", "pause", true] }' | socat - $SOCKET 2>/dev/null
    else
        # Reproducir si no hay ventanas o solo hay kitty
        echo '{ "command": ["set_property", "pause", false] }' | socat - $SOCKET 2>/dev/null
    fi

    sleep 0.5
done

