try:
    a = (raw_input())
    b = (raw_input())
    c = ""
    i=0
    while len(a)>i and len(b)>i:
        c+=chr(97+(ord(a[i])+ord(b[i])-97-97+1)%26);i+=1
    while i<len(a):
        c+=a[i];i+=1
    while i<len(b):
        c+=b[i];i+=1
    print(c)
except:
    print('Invalid Input')
