#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    float arr[1000] = { 0, };
    float num, num1;
    float max = 0, avg = 0;
    scanf("%f", &num);
    for (int i = 0; i < num; i++) {
        scanf("%f", &num1);
        arr[i] = num1;
    }
    
    for (int i = 0; i < num; i++) {
       if (arr[i] >= max) {
           max = arr[i];
        }
    }

    for (int i = 0; i < num; i++) {
        arr[i] = (arr[i] / max) * 100;
    }

    for (int i = 0; i < num; i++) {
        avg += arr[i];
    }

    printf("%f", avg / num);


    
    return 0;
    }
