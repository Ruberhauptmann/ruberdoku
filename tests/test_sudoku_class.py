from ruberdoku import sudoku


def test_index():
    test_sudoku = sudoku.Sudoku()

    all_indeces = [
        test_sudoku.get_sudoku_index(block_number, cell_number)
        for block_number in range(9)
        for cell_number in range(9)
    ]

    assert sorted(all_indeces) == list(range(81))
