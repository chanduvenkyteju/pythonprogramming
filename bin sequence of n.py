N=int(raw_input())
a=[]
for i in range(0,2**N):
    a.clear()
    a.append(format(i,"b"))
    S="".join(map(str,a))
    while(len(S)!=N):
        S='0'+S
    if(i!=(2**N)-1):
        print(S,end=("\n"))
    else:
        print(S)
