import click

from ruberdoku.sudoku import Sudoku


def game_loop(sudoku: Sudoku):
    running = True
    while running:
        print(sudoku)
        block_to_set = click.prompt("Enter block to set", type=int)
        cell_to_change = click.prompt("Enter cell number to set", type=int)
        set_to_value = click.prompt(
            f"Set {block_to_set}, {cell_to_change} to", type=int
        )
        sudoku.set_cell(block_to_set, cell_to_change, set_to_value)
