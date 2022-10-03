#include <stdio.h>
#include <stdlib.h>

int	count_num[1000] = {0,};
int count = 0;
int	ds[4][2] = { {1,0}, {-1,0}, {0,1}, {0,-1} };

void	dfs(char **map, int i, int j, int size)
{
	if (map[i][j] == '0')
		return ;
	if (map[i][j] == '1')
	{
		map[i][j] = '0';
		count++;
	}
	
	for (int k = 0; k < 4; k++)
	{
		int p = i + ds[k][0];
		int q = j + ds[k][1];

		if (p >= 0 && p < size && q >= 0 && q < size)
		{
			dfs(map, p, q, size);
		}
	}
}

void	sort(int num)
{
	int	i;
	int	j;
	int	temp = 0;

	i = 0;
	while (i < num)
	{
		j = i;
		while (j < num)
		{
			if (count_num[i] > count_num[j])
			{
				temp = count_num[i];
				count_num[i] = count_num[j];
				count_num[j] = temp;
			}
			j++;
		}
		i++;
	}
}

int main()
{
	char	**map;
	int	size = 0, num = 0;
	scanf("%d", &size);
	map = (char **)malloc(sizeof(char *) * (size + 1));
	map[size] = 0;
	for (int i = 0; i < size; i++)
	{
		map[i] = (char *)malloc(sizeof(char) * (size + 1));
		map[i][size] = 0;
	}

	for (int i = 0; i < size; i++)
		scanf("%s", map[i]);

	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < size; j++)
		{
			if (map[i][j] == '1')
			{
				dfs(map, i, j, size);
				count_num[num] = count;
				num++;
				count = 0;
			}
		}
	}
	printf("%d\n",num);
	sort(num);
	for (int i = 0; i < num; i++)
		printf("%d\n",count_num[i]);

	for (int i = 0; i < size; i++)
		free(map[i]);
	free(map);
	return (0);
}
