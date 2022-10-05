#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>

int main()
{	
	int N, t;
	char k1, k2, d1, d2, king[3], stone[3],move[3], a, b;

	scanf("%s %s %d", king, stone, &N);
	k1 = king[0];
	k2 = king[1];
	d1 = stone[0];
	d2 = stone[1];
	while (N--)
	{
		scanf("%s", move);
		a = 0; b = 0;
		if (move[0] == 'R') a = 1;
		if (move[0] == 'L') a = -1;
		if (move[0] == 'B' || move[1] == 'B')b = -1;
		if (move[0] == 'T' || move[1] == 'T')b = 1;
		if (k1 + a == d1 && k2 + b == d2)
		{
			if (d1 + a <= 'H' && d1 + a >= 'A' && d2 + b <= '8' && d2 + b >= '1') { 
				k1 += a; d1 += a; k2 += b; d2 += b; 
			}
		}
		else if (k1 + a <= 'H' && k1 + a >= 'A' && k2 + b <= '8' && k2 + b >= '1') {
			k1 += a; k2 += b; 
		}
		memset(move, 0, 3);
	}
	printf("%c%c\n%c%c", k1, k2, d1, d2);
}
