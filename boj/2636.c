#include <stdio.h>
#include <stdlib.h>

int count_cheese(int** cheese, int row, int col)
{

	int result = 0;

	for (int i = 0; i < row; i++)
	{
		for (int j = 0; j < col; j++)
		{
			if (cheese[i][j] == 1)
				result++;
		}
	}
	return (result);
}

void	recursive(int** cheese, int** ans, int row, int col, int r, int c)
{
	if (cheese[r][c] == 1)
	{
		ans[r][c] = 1;
		return;
	}
	if (r < row - 1 && r >= 0 && ans[r][c] == 0)
	{
		if (cheese[r][c] == 0)
        {
			recursive(cheese, ans, row, col, r + 1, c);
        }
    }
	if (c < col - 1 && c >= 0 && ans[r][c] == 0)
	{
		if (cheese[r][c] == 0)
        {
			recursive(cheese, ans, row, col, r, c + 1);
        }
	}
    if (r > 0 && r < row && ans[r][c] == 0)
    {
        if (cheese[r][c] == 0)
        {
            recursive(cheese, ans, row, col, r - 1, c);
        }
    }

    if (c > 0 && c < col)
    {
        if (cheese[r][c] == 0)
        {
            recursive(cheese, ans, row, col, r, c - 1);
        }
    }
}

void	remove_cheese(int** cheese, int** ans, int row, int col)
{
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            if (cheese[i][j] == 1 && ans[i][j] == 1)
            {
                cheese[i][j] = 0;
                ans[i][j] = 0;
            }
        }
    }
}

void    print_ans(int **ans, int row, int col)
{
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            printf("%d ", ans[i][j]);
        }
        printf("\n");
    }
    printf("\n\n");
}

int main()
{
	int	row = 0, col = 0, count = 1, time = 0, last = 0;
	int** cheese;
    int** ans;

	scanf("%d %d", &row, &col);
	cheese = (int**)malloc(sizeof(int*) * row);
	ans = (int**)malloc(sizeof(int*) * row);
    for (int i = 0; i < row; i++)
    {
		cheese[i] = (int*)malloc(sizeof(int) * col);
        ans[i] = (int*)malloc(sizeof(int) * col);
    }

    for (int i = 0; i < row; i++)
	{
		for (int j = 0; j < col; j++)
		{
			scanf("%d", &cheese[i][j]);
            ans[i][j] = 0;
		}
	}
	while (1)
	{
		count = count_cheese(cheese, row, col);	
		if (count == 0)
			break;
		recursive(cheese, ans, row, col, 0, 0);
        print_ans(ans,row,col);
        remove_cheese(cheese, ans, row, col);
		last = count;
		time++;
	}
	printf("%d\n%d\n", time, last);
	for (int i = 0; i < col; i++)
    {
		free(cheese[i]);
        free(ans[i]);
    }
    free(cheese);
    free(ans);
	return (0);
}
