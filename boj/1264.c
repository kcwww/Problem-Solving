#include <stdio.h>

int main()
{
	char	str[257];
	int		i;
	int		ans;

	while(1)
	{
		ans = 0;
		fgets(str, sizeof(str), stdin);
		if (str[0] == '#')
			break;
		i = 0;
		while (str[i])
		{
			if (str[i] == 'a' || str[i] == 'A')
				ans++;
			if (str[i] == 'e' || str[i] == 'E')
				ans++;
			if (str[i] == 'i' || str[i] == 'I')
				ans++;
			if (str[i] == 'o' || str[i] == 'O')
				ans++;
			if (str[i] == 'u' || str[i] == 'U')
				ans++;
			i++;
		}
		printf("%d\n", ans);
	}

    return (0);
}
