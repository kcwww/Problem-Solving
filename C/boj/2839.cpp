#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    int n = 0, m = 0;
    int num;
    scanf("%d", &num);
    
    for (int i = (num / 5); i >= 0; i--) {
        if (((num - (5 * i)) % 3) == 0) {
            n = i;
            m = ((num - (5 * i)) / 3);
            break;
        }
    }
    if (n == 0 && m == 0) printf("%d", -1);
    else printf("%d", m + n);

    return 0;
}
