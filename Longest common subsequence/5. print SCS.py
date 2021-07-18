# Given two strings X and Y, print the shortest string that has both X and Y as 
# subsequences. If multiple shortest supersequence exists, print any one of them.

# Example:      X = 'abac'  Y = 'cab'    ->     scs = # cabac


def func(x, y, m, n):
    table = [[0]*(n+1) for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                table[i][j] = 1 + table[i-1][j-1]
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    
    i, j = m, n
    scs = ''
    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:
            scs = x[i-1] + scs
            i -= 1
            j -= 1
        else:
            if table[i-1][j] > table[i][j-1]:
                scs = x[i-1] + scs
                i -= 1
            else:
                scs = y[j-1] + scs
                j -= 1

    # IMPORTANT
    # If Y reaches its end, put remaining characters
    # of X in the result string
    while i > 0:
        scs = x[i-1] + scs
        i -= 1
    
    # If X reaches its end, put remaining characters
    # of Y in the result string 
    while j > 0:
        scs = y[j-1] + scs
        j -= 1

    return scs


x = 'abac'
y = 'cab'
m = len(x)
n = len(y)
print(func(x, y, m, n))

