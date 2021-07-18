# Given two sequence (strings), find the length of longest subsequence present 
# in both sequence.
# Subsequence is sequence which appears in same order but not necessarily contiguous
# subsequences of 'abcde' -> 'abe', 'abc', 'ae', 'acde' and so on.

# Example: string1 = 'abccdhhijel'  and   string2 = 'acehhhjk'
# Common subsequence: 'achhj' so length = 5


# Base condition:
# when any one of the given string is empty -> return 0
# if m == 0 or n == 0:
#   return 0

# Choice diagram:
# string X of length m and string Y of length n

# we always starts with the last emelent of given input.
# if last char of both strings are equal -> we check for remaining len of strings (m-1, n-1)

# If last char does not match, we have two choice here either we take 
# X till end (i.e m) and Y till len-1 (i.e n-1)     
# or we take X till len-1 (i.e m-1) and Y till end (i.e n)



# Recursive solution:
def lcs(x, y, m, n):
    if m == 0 or n == 0:
        return 0
    elif x[m-1] == y[n-1]:
        return 1 + lcs(x, y, m-1, n-1)
    else:
        return max(lcs(x, y, m, n-1), lcs(x, y, m-1, n))

x = 'abcdfejgh'
y = 'bdekihjl'
m = len(x)
n = len(y)
print(lcs(x, y, m, n))


# Memoization method:
table = [[-1]*(n+1) for i in range(m+1)] 
def lcs(x, y, m, n):
    if m == 0 or n == 0:
        return 0
    
    if table[m][n] != -1:
        return table[m][n]
    elif x[m-1] == y[n-1]:
        table[m][n] = 1 + lcs(x, y, m-1, n-1)
        return table[m][n]
    else:
        table[m][n] = max(lcs(x, y, m, n-1), lcs(x, y, m-1, n))
        return table[m][n]

print(lcs(x, y, m, n))

# Top-Down approach
def lcs(x, y, m, n):
    table = [[0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif x[i-1] == y[j-1]:
                table[i][j] = 1 + table[i-1][j-1]
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])

    return table[m][n]

print(lcs(x, y, m, n))
