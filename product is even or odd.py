N=int(raw_input())
a=list(map(int,(raw_input()).split()))
b=1
for i in range(0,N):
    b=b*int(a[i])
if(b%2==0):
    print("even")
else:
    print("odd")
