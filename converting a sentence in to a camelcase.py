def cond(word):
        import re
        return ''.join(x.capitalize() or " " for x in word.split(" ")) 
    
n=input()
print(cond(n))
