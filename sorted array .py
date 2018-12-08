N=int(raw_input())
S=input().split()
count=1
for i in range(1,len(S)-1):
    if(S[i]<=S[i+1]):
        count=count+1
if(count==len(S)):
    print("yes")
else:
    print("no")
