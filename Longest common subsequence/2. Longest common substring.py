# Given two strings, find length of longest common substring of both strings
# Input : X = 'abcdxyz', y = 'xyzabcd' 
# Output : 4    (abcd)

# common substrings are: ['a', 'b', 'c', 'd', 'x', 'y', 'z', 'ab', 'bc', 'cd', 
# 'xy', 'yz', 'abc', 'bcd', 'xyz', 'abcd']


# Solution:
# Base condition is similar to LCS. when any one string is empty, return 0
# Choice diagram is lil bit different. when last char of each string matches, 
#   we return 1 + table[i-1][j-1] (or return 1 + func(x, y, m-1, n-1))
#   in this case, check the length of substring
#   and when it does not match then we've to reduce length = 0


# Recursive solution:
def func(m, n, leng):
    if m == 0 or n == 0:
        return leng
    if x[m - 1] == y[n - 1]:
        leng = func(m - 1, n - 1, leng + 1)
 
    leng = max(leng, max(func(m, n - 1, 0), func(m - 1, n, 0)))
 
    return leng

x = 'abcdxyz'
y = 'xyzabcd'
m = len(x)
n = len(y)
print(func(m, n, 0))

# Top-Down approach
def func(x, y, m, n):
    table = [[0]*(n+1) for i in range(m+1)]
    res = 0
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif x[i-1] == y[j-1]:
                table[i][j] = 1 + table[i-1][j-1]
                res = max(res, table[i][j])
            else:
                table[i][j] = 0
    return res

print(func(x, y, m, n))