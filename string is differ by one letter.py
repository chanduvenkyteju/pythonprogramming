string1=input()
string2=input()
if len(string1) == len(string2):
    count_diffs = 0
    for a, b in zip(string1, string2):
        if a!=b:
            if count_diffs:
                print("no")
            count_diffs += 1
            print("yes")
            
print("no")  
