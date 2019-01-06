S=(raw_input())
sum=''
a=list(reversed(S))
b=''.join(a)
if(S==b):
    for a in range(0,len(S)-1):
        sum=sum+S[a]
    print(sum)
else:
    print(S)
