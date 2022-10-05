#include <stdio.h>
long long numbers[1000001];

int main(void)
{
	long long max, min;
	long long num;

	int count = 0;
	scanf("%lld %lld", &min, &max);
	for (long long i=2; i * i <= max; i++)
		{
			long long x = min / (i * i);
			if (min % (i * i) != 0)
				x++;
			while (x * (i * i) <= max)
				{
					numbers[x * (i * i) - min] = 1;
					x++;
				}
		}
	for (int i = 0; i <= max - min; i++)
		{
			if  (numbers[i] == 0)
				count++;
		}
	printf("%d\n", count);
	return 0;
}
