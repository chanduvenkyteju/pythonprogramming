S=(raw_input())
r=(raw_input())
S=list(S.split("|"))
if len(S[0])==len(S[1]):
    print("Impossible")
if len(S[1])<len(S[0]):
    if len(S[1])+len(r)==len(S[0]):
        g=""
        S[1]=S[1]+r
        g=g+S[0]+"|"+S[1]
        print(g)
    else:
        print("Impossible")
if len(S[0])<len(S[1]):
    if len(S[0])+len(r)==len(S[1]):
        g=""
        S[0]=S[0]+r
        g=g+S[0]+"|"+S[1]
        print(g)
    else:
        print("Impossible")
