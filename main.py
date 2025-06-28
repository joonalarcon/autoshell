import os
import sys
import platform
import subprocess
import time
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.spinner import Spinner
from rich.table import Table

# Importa features_data desde data/features.py
from data.features import features_data

console = Console()

def check_sudo():
    if os.geteuid() != 0:
        console.print("[bold yellow]⚠ Este script necesita permisos de superusuario (sudo). Se solicitará la contraseña.[/bold yellow]")
        os.execvp("sudo", ["sudo", sys.executable] + sys.argv)

check_sudo()

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
            elif "manjaro" in contenido:
                return "arch"
        return "linux"
    except Exception:
        return "linux"

def instalar_paquete(comando):
    try:
        console.print(f"[bold blue]🔧 Ejecutando comando:[/bold blue] {comando}")

        spinner = Spinner("dots", text="Instalando...", style="bold green")
        with console.status(spinner):
            subprocess.run(comando, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        console.print(f"[bold green]✅ Instalado correctamente:[/bold green] [bold]{comando}[/bold]")
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]❌ Error al instalar:[/bold red] [bold]{comando}[/bold]")
        console.print(f"[bold red]Detalles del error:[/bold red] {e}")
    except FileNotFoundError:
        console.print("[bold red]❌ Comando no encontrado:[/bold red] Asegúrate de que el gestor de paquetes está disponible.")
    except Exception as e:
        console.print(f"[bold red]❌ Ocurrió un error inesperado:[/bold red] {e}")

    time.sleep(2)

def menu_instalar_programas(data, feature_key):
    sistema = detectar_sistema()
    distro = detectar_distro_linux() if sistema == "linux" else None

    while True:
        os.system("clear" if os.name == "posix" else "cls")

        table = Table(title=f"[bold magenta]Selecciona un {feature_key.replace('_', ' ')} para instalar[/bold magenta]")
        table.add_column("ID", style="bold cyan", justify="center")
        table.add_column("Nombre", style="bold yellow", no_wrap=True)
        table.add_column("Descripción", style="bold white")
        table.add_column("Compatibilidad", style="bold green", no_wrap=True)

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

            if sistema == "darwin":
                color = "green" if entry.get("darwin") else "red"
                marca = "✅" if entry.get("darwin") else "❌"
                soportes_list.append(f"[bold][{color}]{marca} macOS[/{color}][/bold]")

            if sistema == "linux":
                linux_commands = entry.get("linux")
                if isinstance(linux_commands, dict):
                    for so_key, so_icon in sistemas_mostrar[:-1]:
                        color = "green" if so_key in linux_commands else "red"
                        marca = "✅" if so_key in linux_commands else "❌"
                        soportes_list.append(f"[bold][{color}]{marca} {so_icon}[/{color}][/bold]")
                elif isinstance(linux_commands, str):
                    soportes_list.append("[bold green]✅ Linux Genérico[/bold green]")
                else:
                    soportes_list.append("[bold red]❌ Linux[/bold red]")

            soportes_str = " | ".join(soportes_list)

            table.add_row(str(i), entry["name"], entry["description"], soportes_str)

        console.print(table)
        opcion = Prompt.ask("\n[bold green]Ingresa el número del programa a instalar (o '0' para volver)[/bold green]", default="0")

        if opcion == "0":
            console.print("[bold cyan]Volviendo al menú anterior...[/bold cyan]")
            break

        if opcion.isdigit() and 0 < int(opcion) <= len(keys):
            key = keys[int(opcion) - 1]
            entry = data[key]
            comando = None

            if sistema == "linux":
                linux_data = entry.get("linux")
                if isinstance(linux_data, dict):
                    comando = linux_data.get(distro)
                elif isinstance(linux_data, str):
                    comando = linux_data
            else:
                comando = entry.get("darwin")

            if not comando:
                console.print("[bold yellow]⚠ Este programa no tiene soporte para tu sistema operativo o distro.[/bold yellow]")
                time.sleep(3)
                continue

            instalar_paquete(comando)

        else:
            console.print("[bold red]❌ Opción inválida.[/bold red]")
            time.sleep(2)

def menu_principal():
    while True:
        os.system("clear" if os.name == "posix" else "cls")
        sistema_operativo = platform.system()
        version = platform.release()
        console.print(Panel(f"🖥️ Sistema detectado: [bold cyan]{sistema_operativo} {version}[/bold cyan]", style="bright_blue"))

        table = Table(title="[bold green]Menú Principal[/bold green]")
        table.add_column("ID", style="bold cyan", justify="center")
        table.add_column("Función", style="bold yellow")

        keys = list(features_data.keys())
        for i, key in enumerate(keys, start=1):
            table.add_row(str(i), features_data[key]['name'])

        table.add_row("0", "[bold red]Salir[/bold red]")

        console.print(table)
        opcion = Prompt.ask("\n[bold green]Selecciona una opción[/bold green]", default="0")

        if opcion == "0":
            console.print("[bold red]Saliendo...[/bold red]")
            break
        elif opcion.isdigit() and 0 < int(opcion) <= len(keys):
            key = keys[int(opcion) - 1]
            feature = features_data[key]
            menu_instalar_programas(feature["data"], key)
        else:
            console.print("[bold red]❌ Opción inválida.[/bold red]")
            time.sleep(2)

if __name__ == "__main__":
    console.print(Panel("[bold cyan]🔧 Script de Instalación Automática[/bold cyan]", style="bright_cyan"))
    menu_principal()
