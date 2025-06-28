from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.style import Style

from installers.programs import features_data
import platform
import subprocess

console = Console()

def detectar_sistema():
    return "darwin" if platform.system() == "Darwin" else "linux"

def detectar_distro_linux():
    try:
        with open("/etc/os-release", "r") as f:
            contenido = f.read().lower()
            if "ubuntu" in contenido:
                return "ubuntu"
            elif "debian" in contenido:
                return "debian"
            elif "arch" in contenido:
                return "arch"
            elif "fedora" in contenido:
                return "fedora"
            else:
                return "linux"
    except Exception:
        return "linux"

def instalar_paquete(comando):
    try:
        subprocess.run(comando, shell=True, check=True)
        console.print(f"[bold green]✅ Instalado correctamente:[/] [bold]{comando}[/bold]")
    except subprocess.CalledProcessError:
        console.print(f"[bold red]❌ Error al instalar:[/] [bold]{comando}[/bold]")

def menu_instalar_programas(data):
    sistema = detectar_sistema()
    distro = detectar_distro_linux() if sistema == "linux" else None

    table = Table(title="[bold magenta]Selecciona un programa para instalar[/bold magenta]", title_style="bold magenta")
    table.add_column("[bold cyan]ID[/bold cyan]", justify="center")
    table.add_column("[bold yellow]Nombre[/bold yellow]", justify="left", no_wrap=True)
    table.add_column("[bold white]Descripción[/bold white]", justify="left")
    table.add_column("[bold green]SO compatible (o distribuciones basadas)[/bold green]", justify="left", no_wrap=True)

    sistemas_mostrar = [
        ("debian", "🌀 Debian"),
        ("arch", "🏔️ Arch"),
        ("fedora", "🎩 Fedora"),
        ("darwin", "🍎 macOS"),
    ]

    keys = list(data.keys())
    for i, key in enumerate(keys, start=1):
        entry = data[key]

        soportes_list = []
        distros = entry.get("distros", [])

        for so_key, so_icon in sistemas_mostrar:
            if so_key == "darwin":
                tiene = bool(entry.get("darwin"))
            else:
                tiene = so_key in distros and so_key in entry.get("linux", {})

            if tiene:
                soportes_list.append(f"[bold green]✅ {so_icon}[/bold green]")
            else:
                soportes_list.append(f"[bold red]❌ {so_icon}[/bold red]")

        soportes_str = " | ".join(soportes_list)

        table.add_row(
            f"[bold cyan]{i}[/bold cyan]",
            f"[bold yellow]{entry['name']}[/bold yellow]",
            entry["description"],
            soportes_str,
            end_section=True  # Esto agrega línea horizontal después de cada fila
        )

    console.print(table)
    opcion = Prompt.ask("[bold green]\nIngresa el número del programa a instalar (o '0' para volver)[/bold green]", default="0")

    if opcion.isdigit() and 0 < int(opcion) <= len(keys):
        key = keys[int(opcion) - 1]
        comando = None
        if sistema == "linux":
            distro = detectar_distro_linux()
            comando = data[key]["linux"].get(distro)
        else:
            comando = data[key].get(sistema)

        if comando:
            instalar_paquete(comando)
        else:
            console.print("[bold yellow]⚠ No hay comando disponible para este sistema operativo o distribución.[/bold yellow]")
    else:
        console.print("[bold cyan]Volviendo al menú principal...[/bold cyan]")

def menu_principal():
    while True:
        sistema_operativo = platform.system()
        version = platform.release()
        console.print(Panel(f"🖥️ Sistema detectado: [bold cyan]{sistema_operativo} {version}[/bold cyan]", expand=False, style="bright_blue"))

        table = Table(title="[bold green]Menú Principal[/bold green]", title_style="bold green")
        table.add_column("[bold cyan]ID[/bold cyan]", justify="center")
        table.add_column("[bold yellow]Función[/bold yellow]", justify="left")

        keys = list(features_data.keys())
        for i, key in enumerate(keys, start=1):
            table.add_row(f"[bold cyan]{i}[/bold cyan]", f"[bold yellow]{features_data[key]['name']}[/bold yellow]")

        table.add_row("[bold cyan]0[/bold cyan]", "[bold red]Salir[/bold red]")

        console.print(table)
        opcion = Prompt.ask("[bold green]\nSelecciona una opción[/bold green]", default="0")

        if opcion == "0":
            console.print("[bold red]Saliendo...[/bold red]")
            break
        elif opcion.isdigit() and 0 < int(opcion) <= len(keys):
            key = keys[int(opcion) - 1]
            feature = features_data[key]
            funcion = feature["function"]
            data = feature["data"]
            if funcion == "menu_instalar_programas":
                menu_instalar_programas(data)
            else:
                console.print(f"[bold red]⚠ Función '{funcion}' no implementada aún.[/bold red]")
        else:
            console.print("[bold red]❌ Opción inválida.[/bold red]")

if __name__ == "__main__":
    console.print(Panel("[bold cyan]🔧 Script de Instalación Automática[/bold cyan]", expand=False, style="bright_cyan"))
    menu_principal()
