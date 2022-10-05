#include <stdio.h>

int main()
{
    long long x, y, z, mid, val, ans, l = 1, r = 1000000000;
    scanf("%lld %lld", &x, &y);
    z = (y * 100) / x;

    if(z >= 99)
	{
        printf("-1\n");
        return (0);
    }

	z++;
    while(l <= r)
	{
        mid = (l + r) / 2;
        val = (y + mid) * 100 / (x + mid);
        if (z <= val) 
		{
			r = mid - 1; 
			ans = mid;
		}
        else 
			l = mid + 1;
    }
    printf("%lld\n", ans);
	return (0);
}
