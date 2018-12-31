N=int(raw_input())
if(N>0 and (N & (N-1))==0):
    print("0")
else:
    if(N%2!=0):
        print("1")
    else:
        print("2")
