n=int(raw_input())
O=[]
for i in range(0,n):
    O.append(int(input()))
low=min(O)
high=max(O)
print(low,high)
