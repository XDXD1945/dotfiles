╔════════════════════════════════════════════════════════════════╗
║                   HYPRLAND RICE - PASTEL TUI                   ║
╚════════════════════════════════════════════════════════════════╝

Este Rice está diseñado para Arch Linux usando Hyprland, Eww 
y herramientas personalizadas en Python.

This Rice is designed for Arch Linux using Hyprland, Eww
and custom tools in Python.

═══════════════════╣ Dependencias/Dependencies ╠══════════════════

hyprland, eww, swww, wofi, kitty, pulseaudio, pamixer, 
pavucontrol, iwd, qt6-base, qt6-wayland, kvantum, kvantum-qt5,
python, python-textual, python-pygame, python-customtkinter,
mpvpaper, git, base-devel, 
zen-browser (o cualquier navegador / or any preferred browser),
nvim (o su editor de preferencia / or your preferred editor)

═══════════╣ Instalación y Descarga / Installation ╠══════════════

[ ESPAÑOL ]

# Para una mayor tasa de éxito, la instalación de Arch Linux debe ser lo más limpia posible.

Antes de empezar, asegúrese de tener acceso a AUR (yay/paru).

1. Primero, cree las carpetas necesarias:
   ~/.config (si no existe)
   ~/.apps
   ~/.wallpapers
   ~/themes

   Puede hacerlo con el siguiente comando:
   mkdir -p ~/.config ~/.apps ~/.wallpapers ~/themes

2. Mueva el contenido de las carpetas descargadas a sus rutas correspondientes:
   - El contenido de ".config" va en ~/.config/
   - La carpeta "wifi-TUI" y similares van en ~/.apps/
   - Los archivos de imagen van en ~/.wallpapers/



3. Otorgue permisos de ejecución a los scripts (el código es abierto, puede revisarlo antes de ejecutar):
   sudo chmod +x ~/.config/eww/scripts/*.sh
   sudo chmod +x ~/.config/hypr/mpv-autopause-workspace.sh
   sudo chmod +x ~/.apps/wifi-TUI/main.py

4. Para VSCode/VSCodium, se recomienda el tema "Catppuccin Mocha".

5. Verificación final:
   - Asegúrese de que PulseAudio esté configurado.
   - Active el servicio de red: sudo systemctl enable --now iwd
   - Verifique que no haya errores de escritura en los nombres de las carpetas.

------------------------------------------------------------------

[ ENGLISH ]

# For a higher success rate, the Arch Linux installation should be as pristine as possible.

Before starting, make sure you have an AUR helper (yay/paru) available.

1. First, create the following folders:
   ~/.config (if it doesn't exist)
   ~/.apps
   ~/.wallpapers
   ~/themes

   You can do this with:
   mkdir -p ~/.config ~/.apps ~/.wallpapers ~/themes

2. Place the subfolders into their corresponding locations:
   - Everything inside ".config" goes to ~/.config/
   - Move "wifi-TUI" and other apps to ~/.apps/
   - Wallpapers go to ~/.wallpapers/

3. Grant the necessary execution permissions (the code is not compiled; feel free to read it to ensure it is safe):
   sudo chmod +x ~/.config/eww/scripts/*.sh
   sudo chmod +x ~/.config/hypr/mpv-autopause-workspace.sh
   sudo chmod +x ~/.apps/wifi-TUI/main.py

4. For VSCode/VSCodium, the "Catppuccin Mocha" theme is recommended.

5. Final check:
   - Ensure PulseAudio is correctly configured.
   - Enable the network service: sudo systemctl enable --now iwd
   - Double-check folder names for typos.

═══════════╣ Configuración Visual / Visual Setup ╠══════════════════

[ ESPAÑOL ]

1. Mover Iconos al Sistema (CRÍTICO para Dolphin y Apps GTK/Qt):
   Para que el sistema reconozca los iconos correctamente:
   sudo cp -r ~/themes/yet-another-monochrome-icon-set /usr/share/icons/

2. Configuración de Kvantum (Interfaz de Ventanas):
   Para aplicar el tema Spectrum-Dark-Kvantum:
   - Abra la aplicación "Kvantum Manager".
   - Vaya a la pestaña "Install/Update Theme".
   - En "Select a theme folder", busque y elija: ~/themes/Spectrum-Dark-Kvantum
   - Presione "Install this theme".
   - Luego, vaya a "Change/Delete Theme", seleccione el tema en la lista y presione "Use this theme".

[ ENGLISH ]

1. Move Icons to System (CRITICAL for Dolphin and GTK/Qt Apps):
   For the system to recognize icons correctly:
   sudo cp -r ~/themes/yet-another-monochrome-icon-set /usr/share/icons/

2. Kvantum Configuration (Window Interface):
   To apply the Spectrum-Dark-Kvantum theme:
   - Open the "Kvantum Manager" app.
   - Go to the "Install/Update Theme" tab.
   - Under "Select a theme folder", browse and choose: ~/themes/Spectrum-Dark-Kvantum
   - Click "Install this theme".
   - Then, go to "Change/Delete Theme", select it from the list, and click "Use this theme".

══════════════════════════════════════════════════════════════════

══════════════════════════════════════════════════════════════════
Recuerden que pueden modificarlo a su gusto y distribuirlo, 
siempre mencionando al creador original y los temas de Catppuccin.
Feel free to modify and distribute, as long as you credit 
the creator and the Catppuccin theme components.
══════════════════════════════════════════════════════════════════

═══════════════════════╣ Créditos / Credits ╠══════════════════════

Desarrollador / Developer: 
  • Ricardo-XDXD (Creador de los scripts en Python y este Rice)

Inspiración y Estética / Inspiration and Themes:
  • Catppuccin Team (Por la paleta de colores Mocha)
  • Hyprland Community (Por el Window Manager)
  • Eww (Elkowars Wacky Widgets)
  • Textualize.io (Por la librería Textual de Python)

Licencia / License:
  • MIT License
  • Siéntanse libres de bifurcar (fork) y mejorar este Rice.
  • Feel free to fork and improve this Rice.

══════════════════════════════════════════════════════════════════
                ¡Gracias por usar este setup!
               Thanks for using this setup!
══════════════════════════════════════════════════════════════════
