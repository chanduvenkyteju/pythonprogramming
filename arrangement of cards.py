a,b=map(int,(raw_input()).split())
s=''
k=2
if(a+b<=3):
    for i in range(0,a+b):
        if(i%2!=0):
            s=s+'0'
        else:
            s=s+'1'
else:    
    for i in range(0,a+b):
        if(i==k):
            s=s+'0'
            if(k==b):
                k=k+2
            else:
                k=k+3
        else:
            s=s+'1'
p=len(s)-1
if(int(s[p])==0):
    print('-1')
else:
    print(s)
