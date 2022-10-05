#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int arr[10002] = { 0, };
void primenum(int num) {
    for (int i = 2; i <= num; i++) arr[i] = i;

    for (int i = 2; i <= num; i++) {
        if (arr[i] == 0) continue;
        for (int j = i + i; j <= num; j += i) {
            arr[j] = 0;

        }
    }

}

int main() {
    int num = 0 ,prime = 0, count = 0;
    int arr2[3] = { 0, };
    scanf("%d", &num);
    while (num) {
        scanf("%d", &prime);
        primenum(prime);

        count = (prime / 2);
        
        for (int i = 2; i <= 10000; i++) {
            if (arr[i] >= count) {
                for (int j = i; j >= 0; j--) {
                    if ((arr[i] + arr[j]) == prime) {
                        arr2[0] = arr[j];
                        arr2[1] = arr[i];
                        count = 1;
                        break;
                    }

                }
            }
            if (count == 1) break;
        }

        count = 0;

        printf("%d %d\n", arr2[0], arr2[1]);
        num--;
    }

    

    return 0;
}
