N=int(raw_input())
if(N>0 and (N & (N-1))==0):
    print("0")
else:
    print("1")
