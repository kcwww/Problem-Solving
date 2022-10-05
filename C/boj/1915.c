#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int	check_map(int i, int j, char** map, int **ans)
{
	int	min = 0;

	if (map[i][j] == '0')
		return (0);
	if (i < 1 || j < 1)
		return (1);
	min = ans[i][j - 1];
	if (min > ans[i - 1][j])
		min = ans[i - 1][j];
	if (min > ans[i - 1][j - 1])
		min = ans[i - 1][j - 1];
	return (min + 1);
}

int main()
{
	int	row = 0, col = 0, max = 0;
	char** board;
	int** ans;

	scanf("%d %d", &row, &col);
	board = (char**)malloc(sizeof(char*) * (row + 1));
	ans = (int**)malloc(sizeof(int*) * row);
	board[row] = 0;
	for (int i = 0; i < row; i++)
	{
		board[i] = (char*)malloc(sizeof(char) * (col + 1));
		ans[i] = (int*)malloc(sizeof(int) * col);
		board[i][col] = 0;
	}

	for (int i = 0; i < row; i++)
		scanf("%s", board[i]);

	for (int i = 0; i < row; i++)
	{
		for (int j = 0; j < col; j++)
		{
			ans[i][j] = check_map(i, j, board, ans);
			if (max < ans[i][j])
				max = ans[i][j];
		}
	}
	

	printf("%d\n", max * max);


	for (int i = 0; i < row; i++)
	{
		free(board[i]);
		free(ans[i]);
	}
	free(board);
	free(ans);

	return (0);
}
