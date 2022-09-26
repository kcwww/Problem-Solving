#include <stdio.h>
#include <string.h>

int	check_string(char* a, char* b)
{
	int	a_len;
	int b_len;
	int	result;
	int	min;

	a_len = strlen(a);
	b_len = strlen(b);
	min = a_len;
	for (int i = 0; i <= (b_len - a_len); i++)
	{
		result = 0;
		for (int j = 0; j < a_len; j++)
		{
			if (a[j] != b[j + i])
				result++;
		}
		if (min > result)
			min = result;
	}
	return (min);
}

int main()
{
	char	a[51] = { 0, };
	char	b[51] = { 0, };

	scanf("%s %s", a, b);
	printf("%d\n", check_string(a, b));
}
