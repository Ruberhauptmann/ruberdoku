"""
1. Add a menu to a console application to manage activities.
2. Run a selected function.
3. Clear the output
4. Display the menu again or exit if done is selected
"""
import os
import sys

import click


def display_menu(menu: list):
    for index, (help_text, function) in enumerate(menu):
        print(f"{index} -- {help_text}")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def load_file():
    print("you have selected menu option one")
    input("Press Enter to Continue\n")
    clear_screen()


def done():
    clear_screen()
    print("Goodbye")
    sys.exit()


def main():
    menu_items = [("Load a file", load_file), ("Done", done)]

    while True:
        display_menu(menu_items)
        selection = click.prompt(
            "Select an option",
            show_choices=False,
            type=click.IntRange(0, len(menu_items)),
        )
        selected_value = menu_items[selection][1]
        selected_value()
