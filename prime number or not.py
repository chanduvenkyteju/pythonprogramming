number = int(input( ))
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
         print("yes")
            break
    else:
        print("no")
else:
    print("invalid")
