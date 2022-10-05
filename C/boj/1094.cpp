#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main(){
    int num = 0, count = 0;
    scanf("%d", &num);
    while (num) {
        
        if (num % 2) count++;
        
        num /= 2;

        

    }

    printf("%d", count);


    return 0;
}
