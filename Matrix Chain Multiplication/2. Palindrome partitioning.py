# Given a string, find minimum no of partition to be made so that each string is palindrome
# Example: 'ababbc'     partition:  'aba' 'bb' 'c' -> min partition = 2

def is_palindrome(string):
    return string == string[::-1]

def solve(string, i, j):
    if i >= j or is_palindrome(string[i:j+1]):
        return 0

    minval = 2**32
    for k in range(i, j):
        temp = solve(string, i, k) + solve(string, k+1, j) + 1
        minval = min(minval, temp)
    return minval

string = 'ababbc'
n = len(string)
print(solve(string, 0, n-1))


# Memoization method:
table = [[-1]*(n+1) for i in range(n+1)]
def solve(string, i, j):
    if i >= j or is_palindrome(string[i:j+1]):
        return 0
    
    if table[i][j] != -1:
        return table[i][j]
    minval = 2**32
    for k in range(i, j):
        temp = solve(string, i, k) + solve(string, k+1, j) + 1
        minval = min(minval, temp)
    table[i][j] = minval
    return table[i][j]
    
print(solve(string, 0, n-1))
# This solution gives TLE, so optimised this solution


# Memoization Method 2:
table = [[-1]*(n+1) for i in range(n+1)]
def solve(string, i, j):
    if i >= j or is_palindrome(string[i:j+1]):
        return 0
    
    if table[i][j] != -1:
        return table[i][j]
    minval = 2**32
    for k in range(i, j):
        if table[i][k] != -1:
            left = table[i][k]
        else:
            left = solve(string, i, k)
        
        if table[k+1][j] != -1:
            right = table[k+1][j]
        else:
            right = solve(string, k+1, j)

        temp = left + right + 1
        minval = min(minval, temp)
    table[i][j] = minval
    return table[i][j]

print(solve(string, 0, n-1))



