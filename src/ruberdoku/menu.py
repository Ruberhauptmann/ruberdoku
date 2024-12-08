import os
import sys


def display_menu(menu: list):
    for index, (help_text, function) in enumerate(menu):
        print(f"{index} -- {help_text}")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def done():
    clear_screen()
    print("Goodbye")
    sys.exit()
