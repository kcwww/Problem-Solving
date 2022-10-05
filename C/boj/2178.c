#include <stdio.h>
#include <stdlib.h>

int flag = 0;
int arr[4][2] = { {1,0}, {-1,0}, {0,1}, {0,-1}};

void	dfs(char **maze, int **visit, int row, int col, int r, int c, int count)
{
	int p = 0;
	int q = 0;
	
	if (r == row && c == col)
	{
		flag = 1;
		printf("%d\n", count);
		return ;
	}
	visit[r][c] = 1;

	for (int i = 0; i < 4; i++)
	{
		p = r + arr[i][0];
		q = c + arr[i][1];
		if (p >= 0 && p < row && q >= 0 && q < col && visit[p][q] != 1)
		{
			if (maze[p][q] == '1' && flag == 0)
				dfs(maze, visit, row, col, p, q, count + 1);
		}
	}
	return ;
}

int	main()
{
	int		row = 0, col = 0, num = 0;
	char	**maze;
	int		**visit;

	scanf("%d %d", &row, &col);
	maze = (char **)malloc(sizeof(char *) * (row + 1));
	visit = (int **)malloc(sizeof(int *) * row);
	maze[row] = 0;
	for (int i = 0; i < row; i++)
	{
		maze[i] = (char *)malloc(sizeof(char) * (col + 1));
		visit[i] = (int *)malloc(sizeof(int) * col);
		maze[i][col] = 0;
	}
	for (int i = 0; i < row; i++)
	{
		scanf("%s", maze[i]);
		for (int j = 0; j < col; j++)
			visit[i][j] = 0;
	}
	dfs(maze, visit, row, col, 0, 0, 1);
	for (int i = 0; i < row; i++)
	{
		free(maze[i]);
		free(visit[i]);
	}
	free(maze[row]);
	free(maze);
	free(visit);
	return (0);
}
