from data.programs import install_programs
from data.languages import install_programs as install_languages
from data.network_tools import install_network_tools
from data.customization import install_customization
from data.terminals import install_terminals

features_data = {
    "install_programs": {
        "name": "🧰 Programas útiles",
        "function": "menu_instalar_programas",
        "data": install_programs
    },
    "install_languages": {
        "name": "📚 Lenguajes de programación",
        "function": "menu_instalar_programas",
        "data": install_languages
    },
    "install_network_tools": {
        "name": "📡 Herramientas de red",
        "function": "menu_instalar_programas",
        "data": install_network_tools
    },
    "install_customization": {
        "name": "🎨 Personalización del sistema",
        "function": "menu_instalar_programas",
        "data": install_customization
    },
    "install_terminals": {
        "name": "🖥️ Terminales",
        "function": "menu_instalar_programas",
        "data": install_terminals
    }
}
