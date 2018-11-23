n=int(input())
x=[]
for i in range(0,n):
    x.append(int(input()))
low=min(x)
high=max(x)
print(low,high)
