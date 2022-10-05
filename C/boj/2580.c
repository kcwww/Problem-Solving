#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool flag = false;

typedef struct s_2580
{
	int	row[81];
	int	col[81];
	int	count;
} t_answer;


int	is_promising(int **sudoku, int row, int col)
{
	int	check[10] = {0,};
	for (int i = 0; i < 9; i++)
	{
		check[sudoku[row][i]]++;
	}
	for (int i = 1; i < 10; i++)
		if (check[i] > 1)
			return (0);
	for (int i = 1; i < 10; i++)
		check[i] = 0;

	for (int i = 0; i < 9; i++)
	{
		check[sudoku[i][col]]++;
	}
	for (int i = 1; i < 10; i++)
		if (check[i] > 1)
			return (0);
	for (int i = 1; i < 10; i++)
		check[i] = 0;

	row = row - (row % 3);
	col = col - (col % 3);
	for (int i = row; i < (row + 3); i++)
	{
		for (int j = col; j < (col + 3); j++)
		{
			check[sudoku[i][j]]++;
		}
	}
	for (int i = 1; i < 10; i++)
		if (check[i] > 1)
			return (0);

	return (1);
}

void	recursive(int **sudoku, t_answer answer, int count, int n)
{
	if (n == count)
	{
		flag = true;
		for (int i = 0; i < 9; i++)
		{
			for (int j = 0; j < 9; j++)
				printf("%d ", sudoku[i][j]);
			printf("\n");
		}
		return ;
	}

	for (int i = 1; i < 10; i++)
	{
		sudoku[answer.row[n]][answer.col[n]] = i;
		if (is_promising(sudoku, answer.row[n], answer.col[n]))
		{
			recursive(sudoku, answer, count, n + 1);
		}
		if (flag == true)
			return ;
	}
	sudoku[answer.row[n]][answer.col[n]] = 0;
}

int main()
{
	int **sudoku;
	int	count = 0;
	t_answer answer = { {0,}, {0,}, 0};

	sudoku = (int **)malloc(sizeof(int *) * 9);
	for (int i = 0; i < 9; i++)
		sudoku[i] = (int *)malloc(sizeof(int) * 9);

	for (int i = 0; i < 9; i++)
	{
		for (int j = 0; j < 9; j++)
			scanf("%d", &sudoku[i][j]);
	}
	printf("\n");
	for (int i = 0; i < 9; i++)
	{
		for (int j = 0; j < 9; j++)
		{
			if (sudoku[i][j] == 0)
			{
				answer.row[count] = i;
				answer.col[count] = j;
				count++;
			}
		}
	}

	recursive(sudoku, answer, count, 0);
}