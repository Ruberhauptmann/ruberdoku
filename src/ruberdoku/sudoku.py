class Sudoku:
    def __init__(self):
        self._field = [0 for _ in range(81)]

    @property
    def field(self):
        return self._field

    @field.setter
    def field(self, value: list[int]):
        self._field = value

    def __getitem__(self, idx):
        return self._field[idx]

    def __setitem__(self, idx, value):
        if value not in list(range(9)):
            print(f"Invalid value {value}")
            raise ValueError
        self._field[idx] = value

    @staticmethod
    def get_sudoku_index(block_number, cell_number):
        block_row = block_number // 3
        block_col = block_number % 3

        cell_row_in_block = cell_number // 3
        cell_col_in_block = cell_number % 3

        global_row = block_row * 3 + cell_row_in_block
        global_col = block_col * 3 + cell_col_in_block

        index = global_row * 9 + global_col

        return index

    def is_valid(self) -> bool:
        for block_number in range(9):
            seen_numbers = []
            for cell_number in range(9):
                cell_index = self.get_sudoku_index(block_number, cell_number)
                if self[cell_index] in seen_numbers and self[cell_index] != 0:
                    return False
                seen_numbers.append(self[cell_index])

        for row_number in range(9):
            seen_numbers = []
            for column_number in range(9):
                cell_index = row_number * column_number
                if self[cell_index] in seen_numbers and self[cell_index] != 0:
                    return False
                seen_numbers.append(self[cell_index])

        for column_number in range(9):
            seen_numbers = []
            for row_number in range(9):
                cell_index = row_number * column_number
                if self[cell_index] in seen_numbers and self[cell_index] != 0:
                    return False
                seen_numbers.append(self[cell_index])

        return True

    def set_cell(self, block_number, cell_number, value):
        cell_index = self.get_sudoku_index(block_number, cell_number)
        self[cell_index] = value

    def __repr__(self):
        return_string = ""
        for row_number in range(9):
            if row_number % 3 == 0:
                return_string += "-" * 31
                return_string += "\n"
            for column_number in range(9):
                if column_number % 3 == 0:
                    return_string += "|"
                value = self[row_number * 9 + column_number]
                if value == 0:
                    return_string += "   "
                else:
                    return_string += f" {self[row_number * 9 + column_number]} "
            return_string += "|\n"
        return_string += "-" * 31
        return return_string
