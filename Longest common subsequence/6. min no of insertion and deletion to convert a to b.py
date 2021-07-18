# Given two strings X and Y of size m and n respectively. The task is to insert and 
# delete the minimum number of characters from/in X to transform it into Y. 
# It could be possible that the same character needs to be deleted from one point of 
# X and inserted to some another point.


# Solution: we can't directly convert X -> Y
# first convert X -> lcs then lcs -> Y

# Example:      X: 'abcdxyz'        Y: 'amnoyz'     lcs = 'ayz'
# convert X -> lcs
#   we need to delete 'bcdx' to convert X -> lcs. number of deletions = 4
# convert lcs -> Y
#   now add 'mno' in lcs to make it Y. number of insertions = 3

# So, deletions = len(X) - len(lcs) and insertions = len(Y) - len(lcs)

def func(x, y, m, n):
    table = [[0]*(n+1) for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                table[i][j] = 1 + table[i-1][j-1]
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    
    lcs = table[m][n]
    insertions = n - lcs
    deletions = m - lcs
    return insertions + deletions

x = 'abcdxyz'
y = 'amnoyz'
m = len(x)
n = len(y)
print(func(x, y, m, n))