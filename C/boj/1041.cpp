#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    long long N = 0, N3 = 0, N2 = 0, N1 = 0, sum = 0;
    int max = 0;
    int dice[6] = { 0, };
    scanf("%lld", &N);
    for (int i = 0; i < 6; i++) {
        scanf("%d", &dice[i]);
    }

    N1 = dice[0];
    for (int i = 0; i < 6; i++) {
        N1 = N1 < dice[i] ? N1 : dice[i];
    }

    N2 = dice[0] + dice[1];
    for (int i = 0; i < 6; i++) {
        for (int j = i + 1; j < 6; j++) {
            if ((i == 0 && j == 5) || (i == 1 && j == 4) || (i == 2 && j == 3)) continue;
            N2 = N2 < dice[i] + dice[j] ? N2 : dice[i] + dice[j];
        }
    }


    N3 = dice[0] + dice[1] + dice[2];
    for (int i = 0; i < 6; i++) {
        for (int j = i + 1; j < 6; j++) {
            if (i == 0 && j == 5) continue;
            else if (i == 1 && j == 4) continue;
            else if (i == 2 && j == 3) continue;
            for (int k = j + 1; k < 6; k++) {
                if (i == 0 && k == 5) continue;
                else if (i == 1 && k == 4) continue;
                else if (i == 2 && k == 3) continue;
                if (j == 0 && k == 5) continue;
                else if (j == 1 && k == 4) continue;
                else if (j == 2 && k == 3) continue;
                N3 = N3 < dice[i] + dice[j] + dice[k] ? N3 : dice[i] + dice[j] + dice[k];
            }
        }
    }
    
    if(N > 1) sum = (4 * N3) + N2 * (4 * (N - 2) + 4 * (N - 1)) + N1 * ((N - 2) * (N - 2) + 4 * (N - 2) * (N - 1));
    else if (N == 1) {
        max = dice[0];
        for (int i = 0; i < 6; i++) {
            max = max > dice[i] ? max : dice[i];
        }
        
        for (int i = 0; i < 6; i++) {
            if (dice[i] == max) continue;
            sum += dice[i];
        }
        if (sum == 0) {
            for (int i = 0; i < 5; i++) sum += dice[i];
        }

    }
    printf("%lld", sum);
    




    return 0;
}
