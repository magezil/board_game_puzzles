#include <stdio.h>
#include "board.h"

void print_board(int size, int board[][8])
{
	int i, j;

	for (i = 0; i < size; i++)
	{
		for (j = 0; j < size; j++)
			printf(" %2d ", board[i][j]);
		printf("\n");
	}
}
