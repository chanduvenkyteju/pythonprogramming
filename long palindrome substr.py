def longestPalindrome(N):
        temp = ""
        for i in range(len(N)):
            for j in range(len(N)-1,i-1,-1):
                if(N[i]==N[j]):
                    m=N[i:j+1]
                    if(m ==m[::-1]):
                        if(len(temp) <= len(m)):
                            temp = m
        return temp
N=str(raw_input())
print(longestPalindrome(N))
