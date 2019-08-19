#include <stdio.h>
void main()
{
    int i,n=14,k=10;
    for(i=0;i<=k;i++)
    {
        printf("%d ",n);
        if(i%2==0)
        {
            n=n*2;
        }
        else
        {
            n=n-8;
        }
    }
}
output:
14 28 20 40 32 64 56 112 104 208 200 
 void main()
 {
     int i,n=28,k=10;
     for(i=0;i<=k;i++)
     {
         printf("%d ",n);
         if(i%2==0)
         {
             n=n-3;
         }
         else
         {
             n=n-4;
         }
     }
 }
output:
28 25 21 18 14 11 7 4 0 -3 -7 
 void main()
 {
     int i,k=5,n=3,l=3,j;
     printf("%d",n);
     for(n=3,j=0;j<=k;j++)
     {
         n=n*10;
         l=n+l;
         printf("+%d",l);
     }
 }
output:
3+33+333+3333+33333+333333+3333333

 void main()
 {
    int i,j,n=5,k=1;
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {printf("%d ",k);
        k=k+1;
        }
        printf("\n");
    }
 }
output:
1 2 3 4 5 
6 7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 
21 22 23 24 25 
 void main()
 {
    int i,j,n=5,k;
    for(i=1;i<=n;i++)
    {   k=i;
        for(j=0;j<n;j++)
        {
            printf("%d ",k);
            k=k+1;
        }
        printf("\n");
    }
 }
output:
1 2 3 4 5 
2 3 4 5 6 
3 4 5 6 7 
4 5 6 7 8 
5 6 7 8 9
 void main()
 {
     int i,k=4,j,p=1,l;
     for(i=k-1;i>=0;i--)
     {  
         for(l=1;l<p;l++)
         {
             printf(" ");
         }
         p=p+1;
         for(j=2*i+1;j>0;j--)
         {
             printf("*");
         }
         printf("\n");
     }
 }
output:
*******
 *****
  ***
   *
 void main()
 {
     int i,k=4,j,p=4,l;
     for(i=0;i<k;i++)
     {  
         for(l=1;l<p;l++)
         {
             printf("  ");
         }
         p=p-1;
         for(j=0;j<2*i+1;j++)
         {
             if(j==0 || j==2*i || i==k-1)
                printf("* ");
            else
                printf("  ");
         }
         printf("\n");
     }
 }
output:
      * 
    *   * 
  *       * 
* * * * * * * 
 void main()
 {
     int i,k=4,j,p=4,l;
     for(i=1;i<=k;i++)
     {  
         for(l=1;l<p;l++)
         {
             printf("  ");
         }
         p=p-1;
         for(j=0;j<2*i-1;j++)
         {
            printf("%d ",i);
            
         }
         printf("\n");
     }
 }
 output:
      1 
    2 2 2 
  3 3 3 3 3 
4 4 4 4 4 4 4 
 
 void main()
 {
     int i,j,n=5,k=1;
     for(i=0;i<=n;i++)
     {
         for(j=0;j<=i;j++)
         {
             printf("%d ",k);
             k++;
         }
         printf("\n");
     }
 }
output:
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 21 

 void main()
 {
     int i,j,n=5,k=1,l;
     for(i=1;i<=n;i++)
     {
         k=i;
         l=4;
         for(j=1;j<=i;j++)
         {
             if(j==1)
             {
                printf("%d ",k);
             }
             else
             {
                 k=k+l;
                 printf("%d ",k);
                 l=l-1;
             }
         }
         printf("\n");
     }
 }
 output:
1 
2 6 
3 7 10 
4 8 11 13 
5 9 12 14 15 
 
 

