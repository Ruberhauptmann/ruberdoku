from ruberdoku import sudoku


def test_median_performance(benchmark):
    test_sudoku = sudoku.Sudoku()
    test_sudoku[5] = 5

    @benchmark
    def bench():
        test_sudoku.is_valid()
