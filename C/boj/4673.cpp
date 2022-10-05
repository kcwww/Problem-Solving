#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>



int self_num (int num) {
    int selnum = num;
    while (num > 0) {
        selnum += (num % 10);
        num /= 10;
        
        
    }
    return selnum;
}




int main() {
    int arr[10001] = { 0, };
    for (int j = 1; j < 10001; j++) {
        if (self_num(j) < 10001) arr[self_num(j)]++;
        if (arr[j] == 0) printf("%d\n", j);
    }
    
    
    return 0;
}
