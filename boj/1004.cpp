#define _CRT_SECURE_NO_WARNINGS    
#include <stdio.h>
#include <math.h>


int main() {
    int TC = 0;
    scanf("%d", &TC);
    int x1 = 0, x2 = 0, y1 = 0, y2 = 0, cx = 0,cy = 0,r = 0, rnum = 0,count = 0, sq1 = 0, sq2 = 0;
    for (int i = 0; i < TC; i++) {
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);

        scanf("%d", &rnum);
        for (int j = 0; j < rnum; j++) {
            scanf("%d %d %d", &cx, &cy, &r);
            sq1 = pow(cx - x1, 2) + pow(cy - y1, 2);
            sq2 = pow(cx - x2, 2) + pow(cy - y2, 2);
            r = pow(r, 2);

            if (r > sq1) if (sq2 > r) count++;

            if (r > sq2) if (sq1 > r) count++;

        }
        printf("%d\n", count);
        count = 0;
    }

    return 0;
}
