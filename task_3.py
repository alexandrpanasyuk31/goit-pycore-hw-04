import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)


def show_tree(path, level=0):
    for item in sorted(path.iterdir()):
        space = "   " * level 

        if item.is_dir():
            print(space + Fore.BLUE + "📂 " + item.name)
            show_tree(item, level + 1) 
        else:
            print(space + Fore.GREEN + "📜 " + item.name)


if len(sys.argv) != 2:
    print(Fore.RED + "Укажите путь: python hw03.py /путь/к/папке")
    sys.exit()

path = Path(sys.argv[1])

if not path.exists():
    print(Fore.RED + "Такого пути не существует")
elif not path.is_dir():
    print(Fore.RED + "Это не папка")
else:
    print(Fore.YELLOW + "📦 " + path.name)
    show_tree(path, 1)
