# Given two strings X and Y. The task is to find the length of the longest subsequence 
# of string X which is a substring in sequence Y.

x = "ABCD"
y = "BACDBDCD"
m = len(x)
n = len(y)

MAX = 1000
def func(x, y, m, n):
    table = [[0 for i in range(MAX)] for i in range(MAX)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if(x[j - 1] == y[i - 1]):
                table[i][j] = 1 + table[i - 1][j - 1]
            else:
                table[i][j] = table[i][j - 1]
                 
    ans = 0
    for i in range(1, n + 1):
        ans = max(ans, table[i][m])
    return ans

print(func(x, y, m, n))

