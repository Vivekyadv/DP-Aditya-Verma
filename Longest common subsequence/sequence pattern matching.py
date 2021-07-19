# Given two strings X and Y. Find if X is a subsequence of string Y.

# Solution:
# if we take LCS of X and Y:        range of LCS = 0 to min(len(x), len(y))
# we've to check if X is sequence of Y. So, X is smaller
# Hence, if LCS == len(x) then return True else return False


def func(x , y):
    i = j = 0
    while i < len(x):
        if x[i] == y[j]:
            j += 1
        if j == len(y):
            return True
        i += 1
    return False

x = 'adxcpy'
y = 'axy'
print(func(x, y))


def func(x, y, m, n):
    table = [[0]*(n+1) for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                table[i][j] = 1 + table[i-1][j-1]
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    
    lenLcs = table[m][n]
    return True if lenLcs == m else False 

x = 'axy'
y = 'adxcpy'
m = len(x)
n = len(y)
print(func(x, y, m, n))
