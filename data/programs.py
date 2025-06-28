# data/programs.py
install_programs = {
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
    },
    "htop": {
        "name": "htop",
        "darwin": "brew install htop",
        "linux": {
            "ubuntu": "sudo apt install htop -y",
            "debian": "sudo apt install htop -y",
            "arch": "sudo pacman -S htop --noconfirm",
            "fedora": "sudo dnf install htop -y"
        },
        "description": "Monitor interactivo de procesos.",
        "distros": ["debian", "arch", "fedora"]
    },
    "git": {
        "name": "Git",
        "darwin": "brew install git",
        "linux": {
            "ubuntu": "sudo apt install git -y",
            "debian": "sudo apt install git -y",
            "arch": "sudo pacman -S git --noconfirm",
            "fedora": "sudo dnf install git -y"
        },
        "description": "Sistema de control de versiones distribuido.",
        "distros": ["debian", "arch", "fedora"]
    },
    "vim": {
        "name": "Vim",
        "darwin": "brew install vim",
        "linux": {
            "ubuntu": "sudo apt install vim -y",
            "debian": "sudo apt install vim -y",
            "arch": "sudo pacman -S vim --noconfirm",
            "fedora": "sudo dnf install vim -y"
        },
        "description": "Editor de texto avanzado.",
        "distros": ["debian", "arch", "fedora"]
    },
    "curl": {
        "name": "Curl",
        "darwin": "brew install curl",
        "linux": {
            "ubuntu": "sudo apt install curl -y",
            "debian": "sudo apt install curl -y",
            "arch": "sudo pacman -S curl --noconfirm",
            "fedora": "sudo dnf install curl -y"
        },
        "description": "Herramienta para transferir datos con URLs.",
        "distros": ["debian", "arch", "fedora"]
    },
    "wget": {
        "name": "Wget",
        "darwin": "brew install wget",
        "linux": {
            "ubuntu": "sudo apt install wget -y",
            "debian": "sudo apt install wget -y",
            "arch": "sudo pacman -S wget --noconfirm",
            "fedora": "sudo dnf install wget -y"
        },
        "description": "Descargador de archivos no interactivo.",
        "distros": ["debian", "arch", "fedora"]
    },
    "tmux": {
        "name": "Tmux",
        "darwin": "brew install tmux",
        "linux": {
            "ubuntu": "sudo apt install tmux -y",
            "debian": "sudo apt install tmux -y",
            "arch": "sudo pacman -S tmux --noconfirm",
            "fedora": "sudo dnf install tmux -y"
        },
        "description": "Multiplexor de terminal.",
        "distros": ["debian", "arch", "fedora"]
    },
    "tree": {
        "name": "Tree",
        "darwin": "brew install tree",
        "linux": {
            "ubuntu": "sudo apt install tree -y",
            "debian": "sudo apt install tree -y",
            "arch": "sudo pacman -S tree --noconfirm",
            "fedora": "sudo dnf install tree -y"
        },
        "description": "Muestra directorios en forma de árbol.",
        "distros": ["debian", "arch", "fedora"]
    },
    "neofetch": {
        "name": "Neofetch",
        "darwin": "brew install neofetch",
        "linux": {
            "ubuntu": "sudo apt install neofetch -y",
            "debian": "sudo apt install neofetch -y",
            "arch": "sudo pacman -S neofetch --noconfirm",
            "fedora": "sudo dnf install neofetch -y"
        },
        "description": "Muestra información del sistema en la terminal.",
        "distros": ["debian", "arch", "fedora"]
    },
    "python3": {
        "name": "Python3",
        "darwin": "brew install python",
        "linux": {
            "ubuntu": "sudo apt install python3 -y",
            "debian": "sudo apt install python3 -y",
            "arch": "sudo pacman -S python --noconfirm",
            "fedora": "sudo dnf install python3 -y"
        },
        "description": "Lenguaje de programación Python 3.",
        "distros": ["debian", "arch", "fedora"]
    },
    "nodejs": {
        "name": "Node.js",
        "darwin": "brew install node",
        "linux": {
            "ubuntu": "sudo apt install nodejs -y",
            "debian": "sudo apt install nodejs -y",
            "arch": "sudo pacman -S nodejs npm --noconfirm",
            "fedora": "sudo dnf install nodejs -y"
        },
        "description": "Entorno de ejecución para JavaScript.",
        "distros": ["debian", "arch", "fedora"]
    },
    "docker": {
        "name": "Docker",
        "darwin": "brew install docker",
        "linux": {
            "ubuntu": "sudo apt install docker.io -y",
            "debian": "sudo apt install docker.io -y",
            "arch": "sudo pacman -S docker --noconfirm",
            "fedora": "sudo dnf install docker -y"
        },
        "description": "Contenedores y virtualización ligera.",
        "distros": ["debian", "arch", "fedora"]
    },
    "vim-plug": {
        "name": "Vim Plug",
        "darwin": "curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim",
        "linux": {
            "ubuntu": "curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim",
            "debian": "curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim",
            "arch": "curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim",
            "fedora": "curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim"
        },
        "description": "Gestor de plugins para Vim.",
        "distros": ["debian", "arch", "fedora"]
    },
    "tmuxinator": {
        "name": "Tmuxinator",
        "darwin": "brew install tmuxinator",
        "linux": {
            "ubuntu": "sudo apt install tmuxinator -y",
            "debian": "sudo apt install tmuxinator -y",
            "arch": "sudo pacman -S tmuxinator --noconfirm",
            "fedora": "sudo dnf install tmuxinator -y"
        },
        "description": "Gestor de configuraciones para tmux.",
        "distros": ["debian", "arch", "fedora"]
    },
    "silversearcher-ag": {
        "name": "The Silver Searcher",
        "darwin": "brew install the_silver_searcher",
        "linux": {
            "ubuntu": "sudo apt install silversearcher-ag -y",
            "debian": "sudo apt install silversearcher-ag -y",
            "arch": "sudo pacman -S the_silver_searcher --noconfirm",
            "fedora": "sudo dnf install the_silver_searcher -y"
        },
        "description": "Herramienta de búsqueda rápida similar a ack.",
        "distros": ["debian", "arch", "fedora"]
    },
    "neovim": {
        "name": "Neovim",
        "darwin": "brew install neovim",
        "linux": {
            "ubuntu": "sudo apt install neovim -y",
            "debian": "sudo apt install neovim -y",
            "arch": "sudo pacman -S neovim --noconfirm",
            "fedora": "sudo dnf install neovim -y"
        },
        "description": "Editor de texto moderno basado en Vim.",
        "distros": ["debian", "arch", "fedora"]
    },
    "jq": {
        "name": "jq",
        "darwin": "brew install jq",
        "linux": {
            "ubuntu": "sudo apt install jq -y",
            "debian": "sudo apt install jq -y",
            "arch": "sudo pacman -S jq --noconfirm",
            "fedora": "sudo dnf install jq -y"
        },
        "description": "Procesador de JSON para línea de comandos.",
        "distros": ["debian", "arch", "fedora"]
    },
    "zsh": {
        "name": "Zsh",
        "darwin": "brew install zsh",
        "linux": {
            "ubuntu": "sudo apt install zsh -y",
            "debian": "sudo apt install zsh -y",
            "arch": "sudo pacman -S zsh --noconfirm",
            "fedora": "sudo dnf install zsh -y"
        },
        "description": "Shell potente y extensible.",
        "distros": ["debian", "arch", "fedora"]
    }
}