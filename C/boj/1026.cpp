#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main(){
    int a = 0, b = 0, count = 0;
    int arr[51] = { 0, };
    int brr[51] = { 0, };
    int crr[51] = { 0, };
    int drr[51] = { 0, };
    scanf("%d", &a);

    for (int i = 0; i < a; i++) {
        scanf("%d", &b);
        arr[i] = b;
    }

    for (int i = 0; i < a; i++) {
        scanf("%d", &b);
        brr[i] = b;
    }
    for (int j = 0; j <= 100; j++) {
        for (int i = 0; i < a; i++) {
            if (j == arr[i]) {
                crr[count] = arr[i];
                count++;
            }
        }
    }
    count = 0;

    for (int j = 100; j >= 0; j--) {
        for (int i = 0; i < a; i++) {
            if (j == brr[i]) {
                drr[count] = brr[i];
                count++;
            }
        }
    }

    int sum = 0;
    for (int i = 0; i < a; i++) sum += crr[i] * drr[i];
    printf("%d", sum);


    return 0;
}
