#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    int day, night, des,dates =0;
    scanf("%d %d %d", &day, &night, &des);
    if ((des - day) % (day - night) == 0) {
        dates = (des - day) / (day - night);
        dates++;
    }
    else {
        dates = (des - day) / (day - night);
        dates += 2;
    }
    printf("%d", dates);

    return 0;
}
