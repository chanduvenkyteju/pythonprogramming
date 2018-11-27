N=int(raw_input())
S=(raw_input())
for i in "aeiouAEIOU":
    S=S.replace(i,"")
print(''.join(reversed(S)))
