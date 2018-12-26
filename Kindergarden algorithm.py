n=int(raw_input())
if (n<=1000000000000000000):
    f=1
    for i in range(1,n):
        f=f*i
    print(f+1)
else:
    print("invalid")
