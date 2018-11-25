string1=input()
string2=input()
if len(string1) == len(string2):
    count= 0
    for a, b in zip(string1, string2):
        if a!=b:
            if count:
                print("no")
            count += 1
            print("yes")
            
print("no")  
