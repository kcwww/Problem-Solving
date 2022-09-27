#include <stdio.h>
#include <stdlib.h>

void	dfs(int** ans, int* com, int duo, int computer, int *count, int virus)
{
	for (int i = 0; i < duo; i++)
	{
		for (int j = 0; j < 2; j++)
		{
			if (ans[i][j] == virus && com[ans[i][!j]] == 1)
				ans[i][2] = 1;
			if (ans[i][j] == virus && ans[i][2] == 0)
			{
				*count += 1;
				ans[i][2] = 1;
				com[ans[i][!j]] = 1;
				dfs(ans, com, duo, computer, count, ans[i][!j]);
			}
		}
	}
}

int main()
{
	int	computer = 0, duo = 0, count = 0;
	int** ans;
	int* com;
	scanf("%d", &computer);
	scanf("%d", &duo);
	com = (int*)malloc(sizeof(int) * (computer + 1));
	for (int i = 0; i <= computer; i++)
		com[i] = 0;
	com[1] = 1;
	ans = (int**)malloc(sizeof(int*) * duo);

	for (int i = 0; i < duo; i++)
		ans[i] = (int *)malloc(sizeof(int) * 3);

	for (int i = 0; i < duo; i++)
	{
		scanf("%d %d", &ans[i][0], &ans[i][1]);
		ans[i][2] = 0;
	}
	
	dfs(ans, com, duo, computer, &count, 1);
	printf("%d\n", count);
	for (int i = 0; i < duo; i++)
		free(ans[i]);
	free(ans);
	free(com);
	return (0);
}
