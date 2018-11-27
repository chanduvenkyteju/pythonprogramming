def c(word):
        import re
        return " ".join(x.capitalize() or " " for x in word.split(" ")) 
    
n=(raw_input())
print(c(n))
