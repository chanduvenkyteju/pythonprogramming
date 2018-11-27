N=int(input())
S=input()
for i in "aeiouAEIOU":
    S=S.replace(i,"")
print(''.join(reversed(S)))
