#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main(){

    int N = 0;
    int P[51] = { 0, };
    int A[51] = { 0, };
    
    scanf("%d", &N);

    for (int i = 0; i < N; i++) scanf("%d", &A[i]);
    
    for (int i = 0; i < N; i++)
    {


        for (int j = 0; j < N; j++)
        {
            if (A[i] > A[j])
            {
                P[i]++;
            }
        }
    }
    
    for (int i = 0; i < N; i++) {
        for (int k = i; k < N; k++)
        {
            if (i != k && P[i] == P[k])
            {
                P[k]++;
            }
        }
    }
            

        

    

    for (int i = 0; i < N; i++)
    {
        printf("%d ", P[i]);
    }
    

    return 0;


}
