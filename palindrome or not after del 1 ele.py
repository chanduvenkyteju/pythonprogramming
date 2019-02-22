a=(raw_input())
for i in range(0,len(a)):
    k=a[:i]+a[i+1:]
    if(k[:]==k[::-1]):
        print("YES")
        break
else:
    print("NO")
