n=str(raw_input())
p=n.replace(" ","")
k=len(p)
if(k>1):
    for i in range(2, k):
        if (k % i) == 0:
            print("no")
            break
    else:
        print("yes")
