#include <stdio.h>
#include <stdlib.h>

int ds[8][2] = { {0,1}, {1,1}, {1,0}, {-1,0},{-1,-1},{0,-1}, {-1,1}, {1,-1} };

void	dfs(int** map, int row, int col, int i, int j)
{
	int r = 0, c = 0;
	if (map[i][j] == 0)
		return;
	if (map[i][j] == 1)
		map[i][j] = 0;
	for (int k = 0; k < 8; k++)
	{
		r = ds[k][0];
		c = ds[k][1];
		r += i;
		c += j;
		if (r >= 0 && r < row && c >= 0 && c < col)
		{
			dfs(map, row, col, r, c);
		}
	}
}
int main()
{
	int	col = 0, row = 0, count;
	int** map;
	while (1)
	{
		scanf("%d %d", &col, &row);
		if (col == 0 && row == 0)
			return (0);
		map = (int**)malloc(sizeof(int*) * row);
		for (int i = 0; i < row; i++)
			map[i] = (int*)malloc(sizeof(int) * col);

		for (int i = 0; i < row; i++)
			for (int j = 0; j < col; j++)
				scanf("%d", &map[i][j]);
		count = 0;
		for (int i = 0; i < row; i++)
		{
			for (int j = 0; j < col; j++)
			{
				if (map[i][j] == 1)
				{
					count++;
					dfs(map, row, col, i, j);
				}
			}
		}
		printf("%d\n", count);

		for (int i = 0; i < row; i++)
			free(map[i]);
		free(map);
	}
}
