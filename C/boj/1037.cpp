#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {
    int max = 0, min = 1000000;
    int arr[50] = { 0, };
    int N, D;
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%d", &D);
        arr[i] = D;
    }
    for (int j = 0; j < N; j++) {
        if (max <= arr[j]) {
            max = arr[j];
        }
        if (min >= arr[j]) {
            min = arr[j];
        }
    }
    printf("%d\n", max * min);



    return 0;
}
