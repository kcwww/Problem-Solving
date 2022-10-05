#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    int N = 0, Jimin = 0, Hansoo = 0, count = 1;
    scanf("%d %d %d", &N, &Jimin, &Hansoo);
    while (1) {
        Jimin = (Jimin + 1) / 2;
        Hansoo = (Hansoo + 1) / 2;
        if (Jimin == Hansoo) break;
        count++;
    }
    printf("%d", count);



    return 0;
}
