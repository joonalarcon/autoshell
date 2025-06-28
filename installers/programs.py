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
