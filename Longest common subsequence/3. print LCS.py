# Given two sequence (strings), print the longest common subsequence present.

def func(x, y, m, n):
    table = [[0]*(n+1) for i in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif x[i-1] == y[j-1]:
                table[i][j] = 1 + table[i-1][j-1]
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    
    i, j = m, n
    lcs = ''
    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:
            lcs = x[i-1] + lcs
            i -= 1
            j -= 1
        else:
            if table[i][j-1] > table[i-1][j]:
                j -= 1
            else:
                i -= 1

    return lcs


x = 'acbcf'
y = 'abcdaf'
m = len(x)
n = len(y)
print(func(x, y, m, n))
