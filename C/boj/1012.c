#include <stdio.h>
#include <stdlib.h>

void	dfs(int** farm, int i, int j, int row, int col)
{
	if (farm[i][j] == 0)
		return;
	if (farm[i][j] == 1)
		farm[i][j] = 0;
	if (i > 0 && i < row)
	{
		dfs(farm, i - 1, j, row, col);
	}
	if (i >= 0 && i < row - 1)
	{
		dfs(farm, i + 1, j, row, col);
	}
	if (j > 0 && j < col)
	{
		dfs(farm, i, j - 1, row, col);
	}
	if (j >= 0 && j < col - 1)
	{
		dfs(farm, i, j + 1, row, col);
	}
}

int main()
{
	int	tc = 0, row = 0, col = 0, lettuce = 0, x = 0, y = 0, ans;
	int** farm;

	scanf("%d", &tc);


	while (tc)
	{
		// 행, 열, 배추의 개수
		scanf("%d %d %d", &row, &col, &lettuce);
		farm = (int**)malloc(sizeof(int*) * row);
		for (int i = 0; i < row; i++)
			farm[i] = (int*)malloc(sizeof(int) * col);

		// 밭 초기화
		for (int i = 0; i < row; i++)
			for (int j = 0; j < col; j++)
				farm[i][j] = 0;

		// 배추 입력
		for (int i = 0; i < lettuce; i++)
		{
			scanf("%d %d", &x, &y);
			farm[x][y] = 1;
		}

		//배추심은곳 지우면서 갯수 카운트
		ans = 0;
		for (int i = 0; i < row; i++)
		{
			for (int j = 0; j < col; j++)
			{
				if (farm[i][j] == 1)
				{
					dfs(farm, i, j, row, col);
					ans++;
				}
			}
		}

		//지렁이 갯수 출력
		printf("%d\n", ans);
		for (int i = 0; i < row; i++)
			free(farm[i]);
		free(farm);
		tc--;
	}
}
