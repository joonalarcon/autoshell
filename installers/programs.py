programs_data = {
    "cowsay": {
        "name": "Cowsay",
        "darwin": "brew install cowsay",
        "linux": {
            "ubuntu": "sudo apt install cowsay -y",
            "debian": "sudo apt install cowsay -y",
            "arch": "sudo pacman -S cowsay --noconfirm",
            "fedora": "sudo dnf install cowsay -y"
        },
        "description": "Genera dibujos de vacas con mensajes divertidos.",
        "distros": ["debian", "arch", "fedora"]
    }
}

languages_data = {
    "python3": {
        "name": "Python 3",
        "darwin": "brew install python",
        "linux": {
            "ubuntu": "sudo apt install python3 -y",
            "debian": "sudo apt install python3 -y",
            "arch": "sudo pacman -S python --noconfirm",
            "fedora": "sudo dnf install python3 -y"
        },
        "description": "Lenguaje de programación interpretado.",
        "distros": ["debian", "arch", "fedora"]
    }
}

network_tools_data = {
    "nmap": {
        "name": "Nmap",
        "darwin": "brew install nmap",
        "linux": {
            "ubuntu": "sudo apt install nmap -y",
            "debian": "sudo apt install nmap -y",
            "arch": "sudo pacman -S nmap --noconfirm",
            "fedora": "sudo dnf install nmap -y"
        },
        "description": "Escáner de red.",
        "distros": ["debian", "arch", "fedora"]
    }
}

personalizacion_data = {
    "neofetch": {
        "name": "Neofetch",
        "darwin": "brew install neofetch",
        "linux": {
            "ubuntu": "sudo apt install neofetch -y",
            "debian": "sudo apt install neofetch -y",
            "arch": "sudo pacman -S neofetch --noconfirm",
            "fedora": "sudo dnf install neofetch -y"
        },
        "description": "Información estética del sistema.",
        "distros": ["debian", "arch", "fedora"]
    }
}

terminales_data = {
    "kitty": {
        "name": "Kitty",
        "darwin": "brew install kitty",
        "linux": {
            "ubuntu": "sudo apt install kitty -y",
            "debian": "sudo apt install kitty -y",
            "arch": "sudo pacman -S kitty --noconfirm",
            "fedora": "sudo dnf install kitty -y"
        },
        "description": "Terminal GPU rápida, moderna y con muchas características.",
        "distros": ["debian", "arch", "fedora"]
    },
    "warp": {
        "name": "Warp",
        "darwin": "brew install --cask warp",
        "linux": "",
        "description": "Terminal moderna con interfaz gráfica y AI integrada (solo macOS).",
        "distros": []
    },
    "alacritty": {
        "name": "Alacritty",
        "darwin": "brew install alacritty",
        "linux": {
            "ubuntu": "sudo apt install alacritty -y",
            "debian": "sudo apt install alacritty -y",
            "arch": "sudo pacman -S alacritty --noconfirm",
            "fedora": "sudo dnf install alacritty -y"
        },
        "description": "Terminal GPU acelerada y minimalista.",
        "distros": ["debian", "arch", "fedora"]
    },
    "tilix": {
        "name": "Tilix",
        "darwin": "",
        "linux": {
            "ubuntu": "sudo apt install tilix -y",
            "debian": "sudo apt install tilix -y",
            "arch": "sudo pacman -S tilix --noconfirm",
            "fedora": "sudo dnf install tilix -y"
        },
        "description": "Terminal en mosaico con interfaz GTK+3.",
        "distros": [ "debian", "arch", "fedora"]
    },
    "wezterm": {
        "name": "WezTerm",
        "darwin": "brew install --cask wezterm",
        "linux": {
            "ubuntu": "sudo snap install wezterm --classic",
            "debian": "sudo snap install wezterm --classic",
            "arch": "yay -S wezterm-git",  # Sujeto a AUR
            "fedora": "sudo dnf install wezterm -y"
        },
        "description": "Terminal moderna, rápida y multiplataforma.",
        "distros": [ "debian", "arch", "fedora"]
    },
    "gnome-terminal": {
        "name": "GNOME Terminal",
        "darwin": "",
        "linux": {
            "ubuntu": "sudo apt install gnome-terminal -y",
            "debian": "sudo apt install gnome-terminal -y",
            "arch": "sudo pacman -S gnome-terminal --noconfirm",
            "fedora": "sudo dnf install gnome-terminal -y"
        },
        "description": "Terminal clásica del entorno GNOME.",
        "distros": ["debian", "arch", "fedora"]
    },
    "konsole": {
        "name": "Konsole",
        "darwin": "",
        "linux": {
            "ubuntu": "sudo apt install konsole -y",
            "debian": "sudo apt install konsole -y",
            "arch": "sudo pacman -S konsole --noconfirm",
            "fedora": "sudo dnf install konsole -y"
        },
        "description": "Terminal del entorno KDE Plasma.",
        "distros": ["ubuntu", "debian", "arch", "fedora"]
    }
}


features_data = {
    "install_programs": {
        "name": "🧰 Programas útiles",
        "function": "menu_instalar_programas",
        "data": programs_data
    },
    "install_languages": {
        "name": "📚 Lenguajes de programación",
        "function": "menu_instalar_programas",
        "data": languages_data
    },
    "install_network_tools": {
        "name": "📡 Herramientas de red",
        "function": "menu_instalar_programas",
        "data": network_tools_data
    },
    "install_customization": {
        "name": "🎨 Personalización del sistema",
        "function": "menu_instalar_programas",
        "data": personalizacion_data
    },
    "install_terminals": {
        "name": "🖥️  Terminales",
        "function": "menu_instalar_programas",
        "data": terminales_data
    }
}
