#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main() {
    int* numPtr;
    int num = 0;
    int a = 0, min = 0, max = 1000, S = 0, count = 0;
    scanf("%d", &num);
    numPtr = (int*)malloc(sizeof(int) * num);
    for (int i = 0; i < num; i++) {
        scanf("%d", &a);
        numPtr[i] = a;
    }
    scanf("%d", &S);


    for (int i = 0; i < num; i++) {
        if ((min < numPtr[i]) && (numPtr[i] < S)) min = numPtr[i];
    }
    
    for (int i = 0; i < num; i++) {
        if ((numPtr[i] > S) && (numPtr[i] < max)) max = numPtr[i];
    }
    

    for (int i = min + 1; i < max - 1; i++) {
        for (int j = i + 1; j < max; j++) {
            if ((S >= i) && (S <= j)) count++;
        }


    }
    for (int i = 0; i < num; i++) if (S == numPtr[i]) count = 0;
    printf("%d", count);

    free(numPtr);
    return 0;
}
