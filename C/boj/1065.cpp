#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>



int main()
{
    int num;
    int count = 0;
    int arr[4];
    scanf("%d", &num);
    if (num < 100) {
        printf("%d", num);
    }
    else if(num >= 100) {
        for (int i = 100; i <= num; i++) {
            arr[0] = i % 10;
            arr[1] = (i / 10) % 10;
            arr[2] = ((i / 10) / 10) % 10;
            arr[3] = (((i / 10) / 10) / 10) % 10;
            if ((arr[3] == 0) && (arr[0] - arr[1]) == (arr[1] - arr[2])) {
                count++;
            }
        }
        printf("%d", count + 99);
    }
    


    return 0;
    }
