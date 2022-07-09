#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int arr[1000002] = { 0, };


void primenum() {
    for (int i = 2; i <= 1000000; i++) arr[i] = i;
    for (int i = 2; i <= 1000000; i++) {

        if (arr[i] == 0) continue;
        for (int j = i+i; j <= 1000000; j += i) {
            arr[j] = 0;
        }
    }
}


int main() {
    int N = 0, M = 0;
    scanf("%d %d", &N, &M);
    primenum();
    for (int i = N; i <= M; i++) {
        if (arr[i] != 0) printf("%d\n", i);
    }


    return 0;
}
