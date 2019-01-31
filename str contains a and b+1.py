N=str(raw_input())
if(len(N)==(N.count('a')+N.count('b')+1)):
    print("yes")
elif(len(N)==(N.count('a')+N.count('b'))):
    print("yes")
else:    
    print("no")
