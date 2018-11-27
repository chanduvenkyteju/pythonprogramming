N=int(input())
sum=0
while(N>0):
    m=int(N%10)
    sum=(m*m)+sum
    N=int(m/10)
print(sum+1)
