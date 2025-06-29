# data/languages.py
install_programs = {
    "python3": {
        "name": "Python 3",
        "darwin": "brew install python",
        "linux": {
            "ubuntu": "sudo apt install python3 -y",
            "debian": "sudo apt install python3 -y",
            "arch": "sudo pacman -S python --noconfirm",
            "fedora": "sudo dnf install python3 -y"
        },
        "description": "Versátil, para web, ciencia de datos e IA.",
        "distros": ["ubuntu", "debian", "arch", "fedora"]
    },
    "node": {
        "name": "Node.js (JavaScript Runtime)",
        "darwin": "brew install node",
        "linux": {
            "ubuntu": "sudo apt install nodejs npm -y",
            "debian": "sudo apt install nodejs npm -y",
            "arch": "sudo pacman -S nodejs npm --noconfirm",
            "fedora": "sudo dnf install nodejs npm -y"
        },
        "description": "Entorno JavaScript del lado del servidor.",
        "distros": ["ubuntu", "debian", "arch", "fedora"]
    },
    "java": {
        "name": "Java",
        "darwin": "brew install openjdk",
        "linux": {
            "ubuntu": "sudo apt install openjdk-17-jdk -y",
            "debian": "sudo apt install openjdk-17-jdk -y",
            "arch": "sudo pacman -S jdk17-openjdk --noconfirm",
            "fedora": "sudo dnf install java-17-openjdk -y"
        },
        "description": "Robusto y OO, para empresas y Android.",
        "distros": ["ubuntu", "debian", "arch", "fedora"]
    },
    "csharp": {
        "name": "C#",
        "darwin": "brew install --cask dotnet-sdk",
        "linux": {
            "ubuntu": "sudo apt update && sudo apt install -y dotnet-sdk-8.0",
            "debian": "sudo apt update && sudo apt install -y dotnet-sdk-8.0",
            "arch": "sudo pacman -S dotnet-sdk --noconfirm",
            "fedora": "sudo dnf install dotnet-sdk-8.0 -y"
        },
        "description": "De Microsoft, para Windows, juegos (Unity) y .NET.",
        "distros": ["ubuntu", "debian", "arch", "fedora"]
    },
    "c": {
        "name": "C",
        "darwin": "xcode-select --install",
        "linux": {
            "ubuntu": "sudo apt install build-essential -y",
            "debian": "sudo apt install build-essential -y",
            "arch": "sudo pacman -S gcc make --noconfirm",
            "fedora": "sudo dnf install gcc make -y"
        },
        "description": "Bajo nivel, fundamental para sistemas y embebidos.",
        "distros": ["ubuntu", "debian", "arch", "fedora"]
    },
    "typescript": {
        "name": "TypeScript",
        "darwin": "brew install typescript",
        "linux": {
            "ubuntu": "sudo npm install -g typescript",
            "debian": "sudo npm install -g typescript",
            "arch": "sudo npm install -g typescript",
            "fedora": "sudo npm install -g typescript"
        },
        "description": "JavaScript con tipado estático para grandes proyectos.",
        "distros": ["ubuntu", "debian", "arch", "fedora"]
    },
    "go": {
        "name": "Go",
        "darwin": "brew install go",
        "linux": {
            "ubuntu": "sudo apt install golang -y",
            "debian": "sudo apt install golang -y",
            "arch": "sudo pacman -S go --noconfirm",
            "fedora": "sudo dnf install golang -y"
        },
        "description": "De Google, enfocado en rendimiento y concurrencia.",
        "distros": ["ubuntu", "debian", "arch", "fedora"]
    },
    "kotlin": {
        "name": "Kotlin",
        "darwin": "brew install kotlin",
        "linux": {
            "ubuntu": "sudo snap install kotlin --classic",
            "debian": "sudo snap install kotlin --classic",
            "arch": "sudo pacman -S kotlin --noconfirm",
            "fedora": "sudo dnf install kotlin -y"
        },
        "description": "Moderno para Android, también web y backend.",
        "distros": ["ubuntu", "debian", "arch", "fedora"]
    },
    "php": {
        "name": "PHP",
        "darwin": "brew install php",
        "linux": {
            "ubuntu": "sudo apt install php -y",
            "debian": "sudo apt install php -y",
            "arch": "sudo pacman -S php --noconfirm",
            "fedora": "sudo dnf install php -y"
        },
        "description": "Para desarrollo web del lado del servidor.",
        "distros": ["ubuntu", "debian", "arch", "fedora"]
    },
    "rust": {
        "name": "Rust",
        "darwin": "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh",
        "linux": {
            "ubuntu": "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh",
            "debian": "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh",
            "arch": "sudo pacman -S rust --noconfirm",
            "fedora": "sudo dnf install rust -y"
        },
        "description": "Seguro, rápido y concurrente, sin recolector de basura.",
        "distros": ["ubuntu", "debian", "arch", "fedora"]
    },
    "swift": {
        "name": "Swift",
        "darwin": "xcode-select --install",
        "linux": {
            "ubuntu": "sudo apt install swift -y",
            "debian": "sudo apt install swift -y",
            "arch": "sudo pacman -S swift --noconfirm",
            "fedora": "sudo dnf install swift -y"
        },
        "description": "De Apple, para iOS, macOS y otras plataformas.",
        "distros": ["ubuntu", "debian", "arch", "fedora"]
    },
    "ruby": {
        "name": "Ruby",
        "darwin": "brew install ruby",
        "linux": {
            "ubuntu": "sudo apt install ruby-full -y",
            "debian": "sudo apt install ruby-full -y",
            "arch": "sudo pacman -S ruby --noconfirm",
            "fedora": "sudo dnf install ruby -y"
        },
        "description": "Propósito general, popular por Ruby on Rails.",
        "distros": ["ubuntu", "debian", "arch", "fedora"]
    },
    "r": {
        "name": "R",
        "darwin": "brew install r",
        "linux": {
            "ubuntu": "sudo apt install r-base -y",
            "debian": "sudo apt install r-base -y",
            "arch": "sudo pacman -S r --noconfirm",
            "fedora": "sudo dnf install R -y"
        },
        "description": "Para computación estadística y gráficos.",
        "distros": ["ubuntu", "debian", "arch", "fedora"]
    },
    "dart": {
        "name": "Dart",
        "darwin": "brew install dart",
        "linux": {
            "ubuntu": "sudo apt update && sudo apt install apt-transport-https -y && sudo sh -c 'wget -qO- https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -' && sudo sh -c 'wget -qO- https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_stable.list > /etc/apt/sources.list.d/dart_stable.list' && sudo apt update && sudo apt install dart -y",
            "debian": "sudo apt update && sudo apt install apt-transport-https -y && sudo sh -c 'wget -qO- https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -' && sudo sh -c 'wget -qO- https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_stable.list > /etc/apt/sources.list.d/dart_stable.list' && sudo apt update && sudo apt install dart -y",
            "arch": "sudo pacman -S dart --noconfirm",
            "fedora": "sudo dnf install dart -y"
        },
        "description": "De Google, para web y móvil (Flutter).",
        "distros": ["ubuntu", "debian", "arch", "fedora"]
    },
    "matlab": {
        "name": "MATLAB",
        "darwin": "No hay un comando simple de instalación vía Homebrew; requiere descarga manual y licencia.",
        "linux": {
            "ubuntu": "No hay un comando simple de instalación; requiere descarga manual y licencia.",
            "debian": "No hay un comando simple de instalación; requiere descarga manual y licencia.",
            "arch": "No hay un comando simple de instalación; requiere descarga manual y licencia.",
            "fedora": "No hay un comando simple de instalación; requiere descarga manual y licencia."
        },
        "description": "Para análisis numérico y científico. (Requiere licencia)",
        "distros": []
    },
    "perl": {
        "name": "Perl",
        "darwin": "brew install perl",
        "linux": {
            "ubuntu": "sudo apt install perl -y",
            "debian": "sudo apt install perl -y",
            "arch": "sudo pacman -S perl --noconfirm",
            "fedora": "sudo dnf install perl -y"
        },
        "description": "Lenguaje de proposito general",
        "distros": ["ubuntu", "debian", "arch", "fedora"]
    },
    "lua": {
        "name": "Lua",
        "darwin": "brew install lua",
        "linux": {
            "ubuntu": "sudo apt install lua5.3 -y",
            "debian": "sudo apt install lua5.3 -y",
            "arch": "sudo pacman -S lua --noconfirm",
            "fedora": "sudo dnf install lua -y"
        },
        "description": "Ligero y embebible, popular en juegos y scripting.",
        "distros": ["ubuntu", "debian", "arch", "fedora"]
    },
    "julia": {
        "name": "Julia",
        "darwin": "brew install julia",
        "linux": {
            "ubuntu": "sudo snap install julia --classic",
            "debian": "sudo snap install julia --classic",
            "arch": "sudo pacman -S julia --noconfirm",
            "fedora": "sudo dnf install julia -y"
        },
        "description": "Para computación numérica y científica de alto rendimiento.",
        "distros": ["ubuntu", "debian", "arch", "fedora"]
    },
    "haskell": {
        "name": "Haskell",
        "darwin": "brew install ghc cabal-install",
        "linux": {
            "ubuntu": "sudo apt install haskell-platform -y",
            "debian": "sudo apt install haskell-platform -y",
            "arch": "sudo pacman -S ghc cabal-install --noconfirm",
            "fedora": "sudo dnf install ghc cabal-install -y"
        },
        "description": "Funcional puro, enfocado en inmutabilidad y tipos seguros.",
        "distros": ["ubuntu", "debian", "arch", "fedora"]
    },
    "scala": {
        "name": "Scala",
        "darwin": "brew install scala",
        "linux": {
            "ubuntu": "sudo apt install scala -y",
            "debian": "sudo apt install scala -y",
            "arch": "sudo pacman -S scala --noconfirm",
            "fedora": "sudo dnf install scala -y"
        },
        "description": "Combina OO y funcional, corre en JVM.",
        "distros": ["ubuntu", "debian", "arch", "fedora"]
    },
    "cobol": {
    "name": "COBOL",
    "darwin": "brew install gnu-cobol",
"linux": {
    "ubuntu": "sudo apt install gnucobol -y",
    "debian": "sudo apt install gnucobol -y",
    "arch": "sudo pacman -S gnu-cobol --noconfirm",
    "fedora": "sudo dnf install gnucobol -y"
},
    "description": "Lenguaje clásico para aplicaciones empresariales.",
    "distros": ["ubuntu", "debian", "arch", "fedora"]
}

}