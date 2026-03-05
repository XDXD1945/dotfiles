#!/usr/bin/env python3

import subprocess
import re
import os
import json
import sys

# --- Configuración de Colores ANSI ---
C = {
    "reset": "\033[0m",
    "red": "\033[38;2;243;139;168m",
    "green": "\033[38;2;166;227;161m",
    "yellow": "\033[38;2;249;226;175m",
    "blue": "\033[38;2;137;180;250m",
    "magenta": "\033[38;2;203;166;247m",
    "cyan": "\033[38;2;148;226;213m",
    "white": "\033[38;2;186;194;222m",
    "gray": "\033[38;2;88;91;112m",
}

INTERFACE = "wlan0"
CONFIG_FILE = os.path.expanduser("~/.apps/wifi-TUI/redes_conocidas.json")
IWD_PATH = "/var/lib/iwd/"

# Asegurar que el directorio del config exista
os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)

def cargar_base_datos():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except: return {}
    return {}

def guardar_red(ssid, password):
    data = cargar_base_datos()
    data[ssid] = password
    with open(CONFIG_FILE, 'w') as f:
        json.dump(data, f, indent=4)
    
    # Perfil nativo para iwd (requiere sudo para escribir en /var/lib/iwd)
    iwd_profile = f"{IWD_PATH}{ssid}.psk"
    content = f"[Settings]\nAutoConnect=true\n\n[Security]\nPassphrase={password}\n"
    
    # Intentar escribir el perfil de iwd
    try:
        subprocess.run(['sudo', 'bash', '-c', f'echo "{content}" > "{iwd_profile}"'], check=True)
    except:
        print(f"{C['red']}Aviso: No se pudo crear el perfil en /var/lib/iwd/ (¿falta sudo?){C['reset']}")

def get_networks():
    # Escaneo silencioso
    subprocess.run(["iwctl", "station", INTERFACE, "scan"], capture_output=True)
    result = subprocess.run(["iwctl", "station", INTERFACE, "get-networks"], 
                            capture_output=True, text=True)
    
    networks = []
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    clean_output = ansi_escape.sub('', result.stdout)
    
    for line in clean_output.split('\n'):
        line = line.strip()
        if "psk" in line or "open" in line:
            parts = re.split(r'\s{2,}', line)
            if len(parts) < 3: continue
            
            ssid = parts[0].replace('> ', '').strip()
            net_type = parts[1].strip()
            signal = parts[2].strip()
            networks.append({"ssid": ssid, "type": net_type, "signal": signal})
    return networks

def connect(ssid):
    print(f"\n{C['yellow']}Conectando a {C['cyan']}{ssid}{C['reset']}...")
    process = subprocess.run(["iwctl", "station", INTERFACE, "connect", ssid], 
                            capture_output=True, text=True)
    
    if process.returncode == 0:
        print(f"{C['green']}¡Conectado!{C['reset']}")
        return True
    else:
        print(f"{C['red']}Error: {process.stderr.strip()}{C['reset']}")
        return False

def main():
    while True:
        os.system('clear')
        conocidas = cargar_base_datos()
        
        print(f"{C['magenta']}╔════════════════════════════════════════╗")
        print(f"║       {C['blue']}WIFI MANAGER PRO (iwd){C['magenta']}          ║")
        print(f"╚════════════════════════════════════════╝{C['reset']}\n")
        
        networks = get_networks()
        
        if not networks:
            print(f"{C['red']}No se detectan redes. Reintentando...{C['reset']}")
        else:
            for i, net in enumerate(networks):
                status = f"{C['green']}[✓]{C['reset']}" if net['ssid'] in conocidas else "   "
                print(f"{C['blue']}{i+1:<3} {status} {C['white']}{net['ssid']:<20} {C['cyan']}{net['signal']:<8} {C['gray']}{net['type']}{C['reset']}")

        print(f"\n{C['magenta']}[M]{C['white']} Scan  {C['magenta']}[Q]{C['white']} Salir")
        
        choice = input(f"\n{C['yellow']}Selección: {C['reset']}").lower()

        if choice == 'q':
            print(f"{C['red']}Saliendo...{C['reset']}")
            sys.exit(0)
        elif choice == 'm':
            continue
        else:
            try:
                idx = int(choice) - 1
                target = networks[idx]
                ssid = target['ssid']
                
                if ssid not in conocidas and "psk" in target['type']:
                    passwd = input(f"{C['yellow']}Passphrase para {C['cyan']}{ssid}{C['yellow']}: {C['reset']}")
                    if passwd:
                        guardar_red(ssid, passwd)
                
                connect(ssid)
                input(f"\n{C['gray']}Presiona Enter para continuar...{C['reset']}")
            except (ValueError, IndexError):
                continue

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{C['red']}Interrumpido por el usuario.{C['reset']}")
        sys.exit(0)
