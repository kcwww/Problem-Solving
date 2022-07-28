#define _CRT_SECURE_NO_WARNINGS    
#include <stdio.h>
#include <math.h>


int main() {
    int TC = 0, num = 0;
    scanf("%d", &TC);
    int x1 = 0, x2 = 0, y1 = 0, y2 = 0, r1 = 0, r2 = 0 , range = 0, sq1 = 0, sq2 = 0;
    for (int i = 0; i < TC; i++) {
        scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);
        range = pow(x1 - x2, 2) + pow(y1 - y2, 2);
        sq1 = pow(r1 + r2, 2);
        sq2 = pow(r1 - r2, 2);
        
        if (range == 0 && sq2 == 0) num = -1;
        
        else if (sq1 == range) num = 1;
        else if (range == sq2) num = 1;

        else if (sq1 > range && range > sq2) num = 2;

        else num = 0;



        printf("%d\n", num);
    }

    return 0;
}
