import os
from pathlib import Path
from pygame import mixer
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, ListItem, ListView, Label, ProgressBar
from textual.containers import Horizontal, Vertical

# Configuración de rutas
BASE_DIR = Path(__file__).parent
MUSIC_DIR = BASE_DIR / "music"

class ReproductorTUI(App):
    CSS_PATH = "styles.tcss"
    BINDINGS = [
        ("space", "toggle_pause", "Play/Pause"),
        ("s", "stop", "Stop"),
        ("q", "quit", "Salir")
    ]

    def on_mount(self):
        """Inicializa el mezclador de audio al arrancar."""
        mixer.init()
        self.playing = False

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        
        with Horizontal():
            # Lista de canciones
            with ListView(id="lista-canciones"):
                # Escaneamos la carpeta music/
                archivos = list(MUSIC_DIR.glob("*"))
                for archivo in archivos:
                    if archivo.suffix.lower() in [".mp3", ".ogg", ".wav", ".flac"]:
                        item = ListItem(Label(archivo.stem))
                        # Guardamos la ruta absoluta como atributo del item
                        item.file_path = str(archivo.absolute())
                        yield item
            
            # Panel de control derecho
            with Vertical(id="visor-reproduccion"):
                yield Label("Reproduciendo ahora:", id="info-header")
                yield Label("Selecciona una canción...", id="titulo-actual")
                yield ProgressBar(total=100, show_percentage=False, id="progreso")
        
        yield Footer()

    def on_list_view_selected(self, event: ListView.Selected):
        """Se activa al pulsar Enter sobre una canción."""
        # Recuperamos la ruta que guardamos en compose
        ruta = getattr(event.item, 'file_path', None)
        
        if ruta:
            nombre = Path(ruta).stem
            self.query_one("#titulo-actual").update(f"󰎈 {nombre}")
            
            try:
                mixer.music.load(ruta)
                mixer.music.play()
                self.playing = True
            except Exception as e:
                self.query_one("#titulo-actual").update(f"Error: {e}")

    def action_toggle_pause(self):
        """Lógica de Play/Pause."""
        if self.playing:
            mixer.music.pause()
            self.playing = False
        else:
            mixer.music.unpause()
            self.playing = True

    def action_stop(self):
        mixer.music.stop()
        self.playing = False
        self.query_one("#titulo-actual").update("Reproducción detenida")

    def action_quit(self):
        mixer.music.stop()
        self.exit()

if __name__ == "__main__":
    # Crear carpeta music si no existe
    if not MUSIC_DIR.exists():
        MUSIC_DIR.mkdir(parents=True, exist_ok=True)
    
    app = ReproductorTUI()
    app.run()
