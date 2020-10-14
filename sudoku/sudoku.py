class SudokuBoard(object):
    def __init__(self, board):
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

if __name__ == "__main__":
    # TODO: add a random board generator
    board = [
        [1,2,3,4,5,6,7,8,9],
        [4,5,6,7,8,9,1,2,3],
        [7,8,9,1,2,3,4,5,6],
        [2,3,4,5,6,7,8,9,1],
        [5,6,7,8,9,1,2,3,4],
        [8,9,1,2,3,4,5,6,7],
        [3,4,5,6,7,8,9,1,2],
        [6,7,8,9,1,2,3,4,5],
        [9,1,2,3,4,5,6,7,8]
        ]
    sudoku = SudokuBoard(board)
    print(sudoku)
    print(sudoku.is_valid())
