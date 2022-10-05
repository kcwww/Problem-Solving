#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>


int check(char a[]) {
    int ans = 0;
    for (int j = 0; j < strlen(a); j++) {
        for (int k = 0; k < strlen(a); k++) {
            if (a[j] == a[k]) {
                ans = k - j;
                if (ans > 1) {

                    if (a[k] != a[k - 1]) return 0;

                }

            }
        }
    }
    return 1;
}




int main() {
    int num;
    scanf("%d", &num);
    
    int answ = 0;
    char arr[101] = { 0, };
    for (int i = 0; i < num; i++) {
        scanf("%s", &arr);
        answ += check(arr);
        
    }


    printf("%d", answ);
    return 0;
}
