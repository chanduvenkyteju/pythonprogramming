N=int(raw_input())
S=str(N)
if((S.count("0")+ S.count("1"))==len(str(N))):
    print("yes")
else:
    print("no")
