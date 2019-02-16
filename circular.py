N = 0
E = 1
S = 2
W = 3
def isCircular(P):  
    x = 0
    y = 0
    dir = N 
    for i in range(len(P)):
        move = P[i] 
        if move == 'R': 
            dir = (dir + 1)%4
        elif move == 'L': 
            dir = (4 + dir - 1)%4
        else:
            if dir == N: 
                y += 1
            elif dir == E: 
                x += 1
            elif dir == S: 
                y -= 1
            else: 
                x -= 1
    return (x == 0 and y == 0) 
P =(raw_input())
if isCircular(P): 
    print ("yes")
else: 
    print("no")
