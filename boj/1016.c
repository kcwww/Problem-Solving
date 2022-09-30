#include <stdio.h>

int	check_pow(long long num, long long b)
{
	long long a = 2;
	while ((a * a) <= b)
	{
		if (num % (a * a) == 0)
		{
			return (0);
		}
		a++;
	}
	return (1);
}

int	main()
{
	long long a = 0, b = 0;
	int	count = 0;
	scanf("%lld %lld", &a, &b);
	for (long long i = a; i <= b; i++)
	{
		if (check_pow(i, b))
			count++;
	}
	printf("%d\n", count);
	return (0);
}
