#include <stdio.h>
#include "board.h"

int solve(int, int, int[], int[][8]);
int is_valid(int, int, int[], int[][8]);

/**
 * main - call function to solve knight's tour
 * 	knight's tour is when the knight visits each spot on the board
 *	exactly one time
 *
 * Return: 0 (success)
 */
int main(void)
{
	int n = 8, i, j;
	int pos[] = {0, 0};
	int board[8][8];

	for (i = 0; i < n; i++)
		for (j = 0; j < n; j++)
			board[i][j] = -1;
	board[pos[0]][pos[1]] = 0;
	printf("starting board:\n");
	print_board(n, board);
	solve(1, n, pos, board);
	printf("solved board:\n");
	print_board(n, board);

	return (0);
}

/**
 * solve - solves knight's tour
 * @count: current position of tour
 * @size: size of board
 * @current: current position of knight
 * @board: board
 *
 * Return: 0 if not solved, 1 if solved
 */
int solve(int count, int size, int current[], int board[][8])
{
	int x, y;
	int newpos[2];

	if (count == size * size)
		return (1);
	for (x = 0; x < size; x++)
	{
		for (y = 0; y < size; y++)
		{
			if (board[x][y] == -1 && is_valid(x, y, current, board))
			{
				board[x][y] = count;
				newpos[0] = x;
				newpos[1] = y;
				if (solve(count + 1, size, newpos, board))
					return (1);
				board[x][y] = -1;
			}
		}
	}

	return (0);
}

/**
 * is_valid - check if new position is valid
 * @x: x coordinate of board
 * @y: y coordinate of board
 * @pos: current knight position
 * @board: current board, 1 if there is a queen, 0 otherwise
 *
 * Return: 1 if valid move, 0 otherwise
 */
int is_valid(int x, int y, int pos[], int board[][8])
{
	return (board[x][y] == -1 && 
	((x == pos[0] + 1 && y == pos[1] + 2) || (x  == pos[0] + 1 && y + 2 == pos[1]) ||
	(x + 1 == pos[0] && y == pos[1] + 2) || (x + 1 == pos[0] && y + 2 == pos[1]) ||
	(x == pos[0] + 2 && y == pos[1] + 1) || (x == pos[0] + 2 && y + 1 == pos[1]) ||
	(x + 2 == pos[0] && y == pos[1] + 1) || (x + 2 == pos[0] && y + 1 == pos[1])));
}
