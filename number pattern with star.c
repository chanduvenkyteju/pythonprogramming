#include <stdio.h>
int main()
{
    int n=5,m=5, i, j, k;
    k = 1;
    for(i=1; i<=n; i++)
    {
        for(j=1; j<=m; j++, k++)
        {
            if(j!=1)
                printf("*%d", k);
            else
                printf("%d", k);
        }
        printf("\n");
    }
    return 0;
}
//for higher numbers
#include <stdio.h>
int main()
{
    int n=4,m=4, i, j, k;
    k = 13;
    for(i=1; i<=n; i++)
    {
        for(j=1; j<=m; j++, k++)
        {
            if(j!=1)
                printf("*%d", k);
            else
                printf("%d", k);
        }
        printf("\n");
    }
    return 0;
}
