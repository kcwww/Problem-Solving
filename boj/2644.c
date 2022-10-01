#include <stdio.h>
#include <stdlib.h>

int flag = 0;

void    dfs(int **re, int dest, int src, int num, int count)
{

    if (src == dest)
    {
        printf("%d\n", count);
        flag = 1;
        return ;
    }
    for (int i = 0; i < num; i++)
    {
        if (re[i][0] == src && flag == 0 && re[i][2] == 0)
        {
            re[i][2] = 1;
            dfs(re, dest, re[i][1], num, count + 1);
        }
        else if (re[i][1] == src && flag == 0 && re[i][2] == 0)
        {
            re[i][2] = 1;
            dfs(re, dest, re[i][0], num, count + 1);
        }
    }
}

int main()
{
    int human = 0, one = 0, two = 0, num = 0;
    int **re;

    scanf("%d",&human);
    scanf("%d %d", &one, &two);
    scanf("%d", &num);

    re = (int **)malloc(sizeof(int *) * num);
    for (int i = 0; i < num; i++)
        re[i] = (int *)malloc(sizeof(int) * 3);
    
    for (int i = 0; i < num; i++)
    {
        scanf("%d %d", &re[i][0], &re[i][1]);
        re[i][2] = 0;
    }
    for (int i = 0; i < num; i++)
    {
        if (re[i][0] == one || re[i][1] == one)
        {
            dfs(re, two, one, num, 0);
            break ;
        }
        if (re[i][0] == two || re[i][1] == two)
        {
            dfs(re, one, two, num, 0);
            break ;
        }
    }
    if (flag == 0)
        printf("-1\n");

    for (int i = 0; i < num; i++)
        free(re[i]);
    free(re);
}