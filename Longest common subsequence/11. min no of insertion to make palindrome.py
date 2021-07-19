# Given a string X, find min no of insertion to make this string a palindrome.
# Example:  X = 'acbcbda'    ans = 2

# Explanation-> LPS of X = 'abcba' 
# if we extract (c & d) from X we'll get LPS. That means we've to insert extra (c & d)
# to make X a palindrome.
# after insertion -> 'acdbcbdca'
# So, this question is same as min no of deletion (previous question)


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