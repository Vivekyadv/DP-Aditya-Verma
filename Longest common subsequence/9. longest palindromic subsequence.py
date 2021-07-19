# Given a sequence, find the length of longest palindromic subsequence in it
# Example:      'agbcba'  ->  'abcba' len = 5

# Solution: this problem can be solved using LCS
# but for LCS we need 2 strings but we have one. So derive another str from given str
# string Y: reverse the string X because we have to find palindromi subsequence and 
# palindrome is eaxctly same in reversed order

# X: 'agbcba'    Y: 'abcbga' (reverse of X)
# now find LCS -> 'abcba' which is palindrome 


def func(x, m):
    y = x[::-1]
    n = m
    table = [[0]*(n+1) for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                table[i][j] = 1 + table[i-1][j-1]
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    
    lcs = table[m][n]
    return lcs

x = 'agbcba'
m = len(x)
print(func(x, m))

x = 'amghagbmac'
m = len(x)
print(func(x, m))
