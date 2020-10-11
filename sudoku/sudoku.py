from random import randint

class SudokuBoard(object):
    def __init__(self, board=None):
        if board is None:
            self.board = self.generate_random_board()
        else:
            self.board = board

    def generate_random_board(self):
        """Use random to generate random integers from 1-9
        """
        return [
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
                    return False
        
        # Check cols
        for i in range(9):
            nums = [0 for i in range(9)]
            for j in range(9):
                nums[self.board[j][i]-1] += 1
                if nums[self.board[j][i]-1] > 1:
                    return False

        # Check 3x3 squares
        for i in range(9):
            nums = [0 for i in range(9)]
            for j in range(9):
                nums[self.board[j//3][j%3]-1] += 1
                if nums[self.board[j//3][j%3]-1] > 1:
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
    print(sudoku.is_valid())
