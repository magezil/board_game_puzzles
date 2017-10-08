#include <stdio.h>
#include "board.h"

int solve(int, int, int[][8]);
int is_attacked(int, int, int, int[][8]);

/**
 * main - call function to solve n queens
 * n queens: place n queens on an n x n board such that they cannot 
 *           attack each other
 *
 * Return: 0 (success)
 */
int main(void)
{
	int n = 8;
	int board[8][8] = {0};

	printf("starting board:\n");
	print_board(n, board);
	solve(n, n, board);
	printf("solved board:\n");
	print_board(n, board);

	return (0);
}

/**
 * solve - solves n queens puzzle
 * @queens: number of queens
 * @size: size of board
 * @board: board
 *
 * Return: 0 if not solved, 1 if solved
 */
int solve(int queens, int size, int board[][8])
{
	int x, y;

	if (queens == 0)
		return (1);
	for (x = 0; x < size; x++)
	{
		for (y = 0; y < size; y++)
		{
			if (board[x][y] != 1 && !is_attacked(x, y, size, board))
			{
				board[x][y] = 1;
				if (solve(queens - 1, size, board))
					return (1);
				board[x][y] = 0;
			}
		}
	}

	return (0);
}

/**
 * is_attacked - check if queen will be attacked from given position
 * @x: x coordinate of board
 * @y: y coordinate of board
 * @size: size of board
 * @board: current board, 1 if there is a queen, 0 otherwise
 *
 * Return: 0 if not attacked, 1 otherwise
 */
int is_attacked(int x, int y, int size, int board[][8])
{
	int i, j;

	for (i = 0; i < size; i++)
	{
		if (board[i][y] == 1)
			return (1);
		if (board[x][i] == 1)
			return (1);
		for (j = 0; j < size; j++)
		{
			if ((i + j) == (x + y))
				if (j != y && board[i][j] == 1)
					return (1);
			if ((i - j) == (x - y))
				if (j != y && board[i][j] == 1)
					return (1);
		}
	}
	return (0);
}
