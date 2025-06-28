from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

from installers.programs import features_data
import platform
import subprocess

console = Console()

def detectar_sistema():
    return "darwin" if platform.system() == "Darwin" else "linux"

def instalar_paquete(comando):
    try:
        subprocess.run(comando, shell=True, check=True)
        console.print(f"[green]✅ Instalado correctamente:[/] {comando}")
    except subprocess.CalledProcessError:
        console.print(f"[red]❌ Error al instalar:[/] {comando}")

def menu_instalar_programas(data):
    sistema = detectar_sistema()
    table = Table(title="Selecciona un programa para instalar", title_style="bold magenta")
    table.add_column("ID", justify="center")
    table.add_column("Nombre", justify="left")
    table.add_column("Descripción", justify="left")

    keys = list(data.keys())
    for i, key in enumerate(keys, start=1):
        table.add_row(str(i), data[key]["name"], data[key]["description"])

    console.print(table)
    opcion = Prompt.ask("\nIngresa el número del programa a instalar (o '0' para volver)", default="0")

    if opcion.isdigit() and 0 < int(opcion) <= len(keys):
        key = keys[int(opcion)-1]
        comando = data[key].get(sistema)
        if comando:
            instalar_paquete(comando)
        else:
            console.print("[yellow]⚠ No hay comando disponible para este sistema operativo.[/]")
    else:
        console.print("[cyan]Volviendo al menú principal...[/]")

def menu_principal():
    while True:
        table = Table(title="Menú Principal", title_style="bold green")
        table.add_column("ID", justify="center")
        table.add_column("Función", justify="left")

        keys = list(features_data.keys())
        for i, key in enumerate(keys, start=1):
            table.add_row(str(i), features_data[key]["name"])

        table.add_row("0", "Salir")

        console.print(table)
        opcion = Prompt.ask("\nSelecciona una opción", default="0")

        if opcion == "0":
            console.print("[bold red]Saliendo...[/]")
            break
        elif opcion.isdigit() and 0 < int(opcion) <= len(keys):
            key = keys[int(opcion)-1]
            data = features_data[key]["data"]
            menu_instalar_programas(data)
        else:
            console.print("[red]❌ Opción inválida.[/]")

if __name__ == "__main__":
    console.print(Panel("🔧 [bold cyan]Script de Instalación Automática[/]", expand=False))
    menu_principal()
