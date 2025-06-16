from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

import platform
import subprocess

console = Console()

# Categorías y programas
programs_data = {
    "cowsay": {
        "name": "Cowsay",
        "darwin": "brew install cowsay",
        "linux": "sudo apt install cowsay -y",
        "description": "Genera dibujos de vacas con mensajes divertidos."
    },
    "figlet": {
        "name": "Figlet",
        "darwin": "brew install figlet",
        "linux": "sudo apt install figlet -y",
        "description": "Transforma texto en arte ASCII."
    }
}

languages_data = {
    "python3": {
        "name": "Python 3",
        "darwin": "brew install python",
        "linux": "sudo apt install python3 -y",
        "description": "Lenguaje de programación interpretado."
    },
    "nodejs": {
        "name": "Node.js",
        "darwin": "brew install node",
        "linux": "sudo apt install nodejs -y",
        "description": "Entorno de ejecución para JavaScript."
    }
}

network_tools_data = {
    "nmap": {
        "name": "Nmap",
        "darwin": "brew install nmap",
        "linux": "sudo apt install nmap -y",
        "description": "Escáner de red."
    },
    "net-tools": {
        "name": "Net-Tools",
        "darwin": "",
        "linux": "sudo apt install net-tools -y",
        "description": "Utilidades de red (ifconfig, netstat, etc.)."
    }
}

personalizacion_data = {
    "neofetch": {
        "name": "Neofetch",
        "darwin": "brew install neofetch",
        "linux": "sudo apt install neofetch -y",
        "description": "Muestra información del sistema de forma estética."
    },
    "htop": {
        "name": "htop",
        "darwin": "brew install htop",
        "linux": "sudo apt install htop -y",
        "description": "Monitor interactivo de procesos."
    },
    "bat": {
        "name": "bat",
        "darwin": "brew install bat",
        "linux": "sudo apt install bat -y",
        "description": "Visualizador de archivos mejorado."
    },
    "zsh": {
        "name": "Zsh",
        "darwin": "brew install zsh",
        "linux": "sudo apt install zsh -y",
        "description": "Shell potente y personalizable."
    },
    "powerlevel10k": {
        "name": "Powerlevel10k",
        "darwin": "brew install romkatv/powerlevel10k/powerlevel10k",
        "linux": "git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/.powerlevel10k && echo 'source ~/.powerlevel10k/powerlevel10k.zsh-theme' >> ~/.zshrc",
        "description": "Tema visual para Zsh altamente personalizable."
    }
}

features_data = {
    "install_programs": {
        "name": "Programas útiles",
        "function": "menu_instalar_programas",
        "data": programs_data
    },
    "install_languages": {
        "name": "Lenguajes de programación",
        "function": "menu_instalar_programas",
        "data": languages_data
    },
    "install_network_tools": {
        "name": "Herramientas de red",
        "function": "menu_instalar_programas",
        "data": network_tools_data
    },
    "install_customization": {
        "name": "Personalización del sistema",
        "function": "menu_instalar_programas",
        "data": personalizacion_data
    }
}

def detectar_sistema():
    system = platform.system()
    return "darwin" if system == "Darwin" else "linux"

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
            funcion = features_data[key]["function"]
            data = features_data[key]["data"]
            if funcion == "menu_instalar_programas":
                menu_instalar_programas(data)
        else:
            console.print("[red]❌ Opción inválida.[/]")

if __name__ == "__main__":
    console.print(Panel("🔧 [bold cyan]Script de Instalación Automática[/]", expand=False))
    menu_principal()
