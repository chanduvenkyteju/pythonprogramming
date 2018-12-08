N=int(raw_input())
S=input().split()
c=1
for i in range(1,len(S)-1):
    if(S[i]<=S[i+1]):
        c=c+1
if(c==len(S)):
    print("yes")
else:
    print("no")
