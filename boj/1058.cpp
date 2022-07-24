#define _CRT_SECURE_NO_WARNINGS    
#include <stdio.h>
#include <string.h>    
#include <stdlib.h>

int main() {
    int num = 0;
    scanf("%d", &num);
    int* fri = (int*)malloc(sizeof(int) * num);
    int* max = (int*)malloc(sizeof(int) * num);

    char** arr = (char**)malloc(sizeof(char*) * num);
    for (int i = 0; i < num; i++) arr[i] = (char*)malloc(sizeof(char) * (num+1));

    for (int i = 0; i < num; i++) scanf("%s", arr[i]);
    
    for (int i = 0; i < num; i++) {
        fri[i] = 0;
        max[i] = 0;
    }

    for (int i = 0; i < num; i++) {
        for (int j = 0; j < num; j++) {

            if (arr[i][j] == 'Y') {
                if (arr[j][i] == 'Y') fri[j] = 1;
                for (int k = 0; k < num; k++) {
                    if (k == i) continue;
                    else if (arr[k][j] == 'Y') fri[k] = 1;
                }

            }
        }
        
        for (int z = 0; z < num; z++) max[i] += fri[z];
        for (int z = 0; z < num; z++) fri[z] = 0;

    }

    int maxnum = 0;
    for (int i = 0; i < num; i++) maxnum = maxnum > max[i] ? maxnum : max[i];


    printf("%d", maxnum);


    for (int i = 0; i < num; i++) free(arr[i]);
    free(arr);
    free(fri);
    free(max);


}
