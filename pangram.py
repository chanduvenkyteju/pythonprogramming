S=(raw_input())
k=[]
for i in s:
    if(i not in k):
        k.append(i)
if(len(k)==27 or len(k)==28):
    print("yes")
else:
    print("no")
