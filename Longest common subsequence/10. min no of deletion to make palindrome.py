# Given a string X, return minimum number of deletion to make this string a palindrome
# Example: X = 'agbchba'    ans = 2, palindrome = 'abcba' or 'abhba'

# string = 'agbcba'
# palindromes of given string are -> 'bcb' (require 3 deletions), 
# 'abba' (require 2 deletions), 'abcba' (require 1 deletion)
# So, min no of deletions = 1

# Conclusion: min no of deletions gives longest palindromic subsequence, so this question
# can be solved using LPS.
# min no of deletion = length of string - LPS 

def func(x, n):
    y = x[::-1]
    table = [[0]*(n+1) for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                table[i][j] = 1 + table[i-1][j-1]
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    
    return n - table[n][n]

x = 'agbchba'
n = len(x)
print(func(x, n))
