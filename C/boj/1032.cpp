#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){
    int num = 0;
    scanf("%d", &num);
    char** arr = (char**)malloc(sizeof(char*) * num);
    for (int i = 0; i < num; i++) {
        arr[i] = (char*)malloc(sizeof(char) * 51);
    }

    for (int i = 0; i < num; i++) {
        scanf("%s", arr[i]);
    }

    int a = strlen(arr[0]);
    for (int i = 0; i < num; i++) {
        if (strcmp(arr[0], arr[i]) != 0) {
            for (int j = 0; j < a; j++) {
                if (arr[0][j] != arr[i][j]) arr[0][j] = '?';
            }
        }
    }

    printf("%s", arr[0]);

    
    for (int i = 0; i < num; i++) free(arr[i]);
    free(arr);


    return 0;
}
