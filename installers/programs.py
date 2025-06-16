import platform
import subprocess
from rich.console import Console
from rich.table import Table

console = Console()

# Datos "JSON" embebidos como diccionario Python
programs_data = {
    "cowsay": {
        "name": "Cowsay",
        "darwin": "brew install cowsay",
        "linux": "sudo apt install cowsay -y"
    },
    "zsh": {
        "name": "Zsh",
        "darwin": "brew install zsh",
        "linux": "sudo apt install zsh -y"
    },
    {
        "name": "Neofetch",
        "darwin": "brew install neofetch",
        "linux": "sudo apt install neofetch -y"
    }
}

def list_programs():
    table = Table(title="Programas disponibles", expand=False, border_style="cyan")
    table.add_column("Opción", style="bold yellow", justify="center")
    table.add_column("Programa", style="bold green")

    keys = list(programs_data.keys())
    for idx, key in enumerate(keys, 1):
        table.add_row(str(idx), programs_data[key]["name"])
    table.add_row(str(len(keys)+1), "Salir")
    console.print(table)
    return keys

def install_program(key):
    sistema = platform.system()
    data = programs_data.get(key)

    if not data:
        console.print(f"[bold red]Programa '{key}' no encontrado.[/bold red]")
        return

    if sistema == "Darwin":
        comando = data.get("darwin")
    elif sistema == "Linux":
        comando = data.get("linux")
    else:
        console.print("[bold red]Sistema no compatible automáticamente.[/bold red]")
        return

    if not comando:
        console.print(f"[bold red]No hay comando para instalar {data['name']} en {sistema}.[/bold red]")
        return

    table = Table(title=f"Instalador {data['name']}", expand=False, border_style="cyan")
    table.add_column("Opción", style="bold yellow", justify="center")
    table.add_column("Comando", style="bold green")
    table.add_row("1", comando)
    console.print(table)

    console.print("[bold green]¿Desea ejecutar la instalación ahora? (s/n):[/bold green]")
    choice = input("> ").strip().lower()
    if choice == "s":
        console.print("[bold cyan]Ejecutando instalación...[/bold cyan]")
        subprocess.run(comando, shell=True)
    else:
        console.print("[bold red]Instalación cancelada.[/bold red]")
