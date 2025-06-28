# data/terminals.py
install_terminals = {
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
        "linux": "", # Considera agregar instrucciones para Linux si existen alternativas
        "description": "Terminal moderna con interfaz gráfica y AI integrada.",
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
        "darwin": "", # No hay un comando simple de instalación para macOS
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
        "darwin": "", # No se instala comúnmente en macOS
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
        "darwin": "", # No se instala comúnmente en macOS
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