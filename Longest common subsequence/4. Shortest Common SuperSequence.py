# Given two strings str1 and str2, the task is to find the length of the shortest 
# string that has both str1 and str2 as subsequences.

# str1 = "AGGTAB",  str2 = "GXTXAYB"
# 'AGXGTXAYB' is sorted common supersequence -> length = 9


def func(x, y, m, n):
    table = [[0]*(n+1) for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                table[i][j] = 1 + table[i-1][j-1]
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    
    lcs = table[m][n]
    return m + n - lcs

x = 'AGGTAB'
y = 'GXTXAYB'
m = len(x)
n = len(y)
print(func(x, y, m, n))


# Method 2: 
def func(x, y, m, n):
    table = [[0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if not i:
                table[i][j] = j
            elif not j:
                table[i][j] = i
            elif x[i-1] == y[j-1]:
                table[i][j] = 1 + table[i-1][j-1]
            else:
                table[i][j] = 1 + min(table[i-1][j], table[i][j-1])

    return table[m][n]

print(func(x, y, m, n))
