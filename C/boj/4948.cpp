#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int arr[246914] = { 0, };
int num = 123456;

void primenum() {
    for (int i = 2; i <= num*2; i++) arr[i] = i;
    for (int i = 2; i <= num*2; i++) {

        if (arr[i] == 0) continue;
        for (int j = i+i; j <= num*2; j += i) {
            arr[j] = 0;
        }
    }
}


int main() {
    int N = 1, count = 0;
    
    primenum();
    while (1) {
        scanf("%d", &N);
        if (N == 0) break;

        for (int i = N+1; i <= (2 * N); i++) {
            if (arr[i] != 0) count++;
        }
        printf("%d\n", count);
        count = 0;
    }

    


    return 0;
}
