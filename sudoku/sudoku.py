from random import shuffle

class SudokuBoard(object):
    def __init__(self, board=None):
        if not board:
            self.board = self.generate_random_board()
        else:
            self.board = board

    def __str__(self):
        lines = []
        for i in range(len(self.board)):
            lines.append(' '.join(map(str, self.board[i])))
        return str('\n'.join(lines))

    def __repr__(self):
        return {'board': self.board}

    def generate_random_board(self):
        """Use random to generate random integers from 1-9
        """
        print('Generating a random board')
        nums = list(range(1, 10))
        random_board = []
        for _ in range(9):
            shuffle(nums)
            random_board.append(nums.copy())
        return random_board

    def generate_partially_board(self):
        """Possibly generate a random board with some numbers missing
        or have a bunch of pregenerated solveable boards
        or write solver first, use the generate_random_board and delete some numbers,
            check to see if board is solveable using solver
        """
        pass

    def is_valid(self):
        """Check if board is valid
        """
        # Assume square board
        if len(self.board) != 9 or len(self.board[0]) != 9:
            return False
        # TODO: make this more efficient
        # Check rows
        for i in range(9):
            nums = [0 for i in range(9)]
            for j in range(9):
                nums[self.board[i][j]-1] += 1
                if nums[self.board[i][j]-1] > 1:
                    print(f'Row failed on {i}, {j}: {self.board[i][j]}')
                    return False
        
        # Check cols
        for i in range(9):
            nums = [0 for i in range(9)]
            for j in range(9):
                nums[self.board[j][i]-1] += 1
                if nums[self.board[j][i]-1] > 1:
                    print(f'Column failed on {j}, {i}: {self.board[j][i]}')
                    return False

        # Check 3x3 squares
        for i in range(9):
            nums = [0 for i in range(9)]
            for j in range(9):
                nums[self.board[j//3][j%3]-1] += 1
                if nums[self.board[j//3][j%3]-1] > 1:
                    print(f'Square failed on {j//3}, {j%3}: {self.board[j][i]}')
                    return False
        return True

    def sudoku_solver(self):
        """Solve a sudoku puzzle
        """
        # TODO
        pass

if __name__ == "__main__":
    sudoku = SudokuBoard()
    print(sudoku.__str__())
    print(sudoku.is_valid())
