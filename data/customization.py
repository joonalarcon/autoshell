# data/personalization.py
install_customization = {
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