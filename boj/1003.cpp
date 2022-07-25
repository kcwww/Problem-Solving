#define _CRT_SECURE_NO_WARNINGS    
#include <stdio.h>

int main() {
    int num = 0, t = 0;
    int one[41] = { 0,1, };

    scanf("%d", &t);
        for (int i = 0; i < t; i++) {
            scanf("%d", &num);

            for (int j = 2; j <= num; j++) one[j] = one[j - 2] + one[j - 1];
                if(num == 0) printf("%d %d\n", 1, one[num]);

                else printf("%d %d\n", one[num-1], one[num]);
            }
    return 0;
    }
