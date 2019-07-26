// numbers increment in rows and columns
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
// two arrows of stars
#include <stdio.h>
int main()
{
    int n=5,i, j,k,l,m,p,q;
    for(i=n; i>0; i--)
    {
        for(j=1; j<=i; j++)
        {
            printf("*");
        }
        for(l=i;l<n;l++)
        {
            printf(" ");
        }
        for(j=1; j<=i; j++)
        {
            printf("*");
        }
        if(i!=1)
        printf("\n");
    }
    for(m=0;m<=n;m++)
    {
        for(k=0;k<m;k++)
        {
            printf("*");
        }
        for(p=m;p<n;p++)
        {
            printf(" ");
        }
        for(q=1; q<=m; q++)
        {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}

// diamond outline in box
#include <stdio.h>
int main()
{
    int n=5,i,j,k,l;
    for(i=n; i>0; i--)
    {
        for(j=1; j<=i; j++)
        {
            printf("*");
        }
        for(k=i*2;k<n*2;k++)
        {
            printf(" ");
        }
        for(l=1; l<=i; l++)
        {
            printf("*");
        }
        if(i!=1)
        printf("\n");
    }
    for(i=0;i<=n;i++)
    {
        for(j=0;j<i;j++)
        {
            printf("*");
        }
        for(k=n*2;k>i*2;k--)
        {
            printf(" ");
        }
        for(l=1; l<=i; l++)
        {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}

