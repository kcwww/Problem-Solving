#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){
    int count = 1, row = 0 , col = 0, num = 0;
    scanf("%d %d", &row, &col);
    num = row > col ? col : row;
    char** arr = (char**)malloc(sizeof(char*) * row);
    for (int i = 0; i < row; i++) {
        arr[i] = (char*)malloc(sizeof(char) * (col+1));
    }

    for (int i = 0; i < row; i++) scanf("%s", arr[i]);

    
    for (int i = 0; i < row; i++) { //012 행변환

        for (int j = 0; j < col; j++) { //01234 열변환

            for (int k = 1; k < num; k++) { //정사각형 크기변환
                if ((i + k) >= row || (j + k) >= col) break;
                

                if ((arr[i][j] == arr[i + k][j + k]) && (arr[i + k][j] == arr[i][j + k]) && (arr[i][j] == arr[i + k][j])) {
                    count = count > (k + 1) ? count : k + 1;
                }

              
            }


        }

    }



    printf("%d", count*count);




    for (int i = 0; i < row; i++) free(arr[i]);
    free(arr);

    return 0;
}
