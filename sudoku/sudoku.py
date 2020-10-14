from random import randint, shuffle

class SudokuBoard(object):
    def __init__(self, board=None):
        if not board:
            self.board = self.generate_random_board()
        else:
            self.board = board

    def __str__(self):
        """Return board as a string
        """
        lines = [''.join(['-' for i in range(9 + 2 + 10)])]
        for i in range(len(self.board)):
            line = []
            for k in range(len(self.board[i])):
                if k != 0 and k % 3 == 0:
                    line.append('|')
                line.append(self.board[i][k])
            if i != 0 and i % 3 == 0:
                lines.append('------+-------+------')
            lines.append(' '.join(map(str, line)))
        lines.append(''.join(['-' for i in range(9 + 2 + 10)]))
        return str('\n'.join(lines))

    def __repr__(self):
        """Return representation of sudoku board
        """
        return {'board': self.board}

    def generate_random_board(self):
        """Use random to generate random integers from 1-9
        """
        print('Generating a random board')
        # nums = list(range(1, 10))
        # TODO: try to make it more likely to get a valid board after write solver.
        # Start with a random number in a random spot. Add random number and keep backtracking to see if still valid.
        random_board = []
        for _ in range(9):
            nums = [randint(1, 9) for i in range(9)]
            # shuffle(nums)
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
    print(sudoku)
    print(sudoku.is_valid())

    # count = 0
    # while not sudoku.is_valid():
    #     sudoku.board = sudoku.generate_random_board()
    #     print(sudoku)
    #     count += 1
    #     print(count)
