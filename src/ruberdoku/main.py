"""
1. Add a menu to a console application to manage activities.
2. Run a selected function.
3. Clear the output
4. Display the menu again or exit if done is selected
"""
import click

from ruberdoku.game_loop import game_loop
from ruberdoku.menu import clear_screen, display_menu, done
from ruberdoku.sudoku import Sudoku


def load_file():
    sudoku = Sudoku()
    game_loop(sudoku)
    clear_screen()


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
