# data/network_tools.py
install_network_tools = {
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