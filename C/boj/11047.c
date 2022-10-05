#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main()
{
	int	coin = 0, price = 0, c = 0;
	int* coins;

	scanf("%d %d", &coin, &price);

	coins = (int*)malloc(sizeof(int) * coin);

	for (int i = 0; i < coin; i++)
	{
		scanf("%d", &c);
		coins[i] = c;
	}

	int	count = 0;
	while (price)
	{
		int	i = coin - 1;
		while (price < coins[i])
		{
			i--;
		}
		int	j = 1;
		while (price >= (coins[i]) * j)
		{
			j++;
		}
		j--;
		price = price - (coins[i] * j);
		count += j;
	}
	
	
	printf("%d\n", count);
	free(coins);
}
