# data/network_tools.py
install_network_tools = {
    "nmap": {
        "name": "Nmap",
        "darwin": "brew install nmap",
        "linux": {
            "debian": "no disponible",
            "arch": "no disponible",
            "fedora": "no disponible"
        },
        "description": "Escáner de red.",
        "distros": ["debian", "arch", "fedora"]
    }
}