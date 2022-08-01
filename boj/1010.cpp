#define _CRT_SECURE_NO_WARNINGS    
#include <stdio.h>


int main()
{
	int TC = 0, left = 0, right = 0, answer = 1;
	scanf("%d", &TC);
	int rightp = 0;
	while (TC)
	{
		scanf("%d %d", &left, &right);
		rightp = right;
		for (int i = 1; i <= left; i++)
		{
			answer = (answer * rightp) / i;
			rightp--;
		}
		printf("%d\n", answer);
		answer = 1;
		TC--;
	}

	return 0;
}
