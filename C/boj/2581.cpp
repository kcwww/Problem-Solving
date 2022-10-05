#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int arr[10000] = { 0, };
    int min = 10000, a=0,b=0;
    int count = 0, c = 0, sum = 0;
    scanf("%d", &a);
    scanf("%d", &b);
    for (int i = a; i <= b; i++) {
        for (int j = 1; j < i; j++) {
            if ((i % j) == 0)count++;
        }
        if (count == 1) {
            arr[c] = i;
            c++;
        }
        count = 0;
        
    }
    c = 0;
    if (arr[c] == 0) printf("%d", -1);
    else {
        while (1) {
            sum += arr[c];
            min = min > arr[c] ? arr[c] : min;
            c++;
            if (arr[c] == 0) break;

        }
        printf("%d\n%d", sum, min);
    }
    

    return 0;
}
