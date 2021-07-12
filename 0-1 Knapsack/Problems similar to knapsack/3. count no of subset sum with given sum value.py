# Given an array and sum value x, find number of subsets whose sum = x

# This problem is similar to subset sum problem. Instead of returning True or False, 
# we have to count number of subsets whose sum = x

# Variation in code:
# 1. Initialization: create table[n+1][x+1] but instead of filling it with True or False
#    we fill it with 1 and 0. False means we can't create subset, so number of subsets
#    with sum = x is 0. and True means we can create at least empty subset that means
#    at least 1 subset with sum = 0 (first column of table).
# 2. Main code: In subset sum problem when we found a subset whose sum = x then we return
#    True. But in this problem even after finding such subset, we have to search further.
#    So, instead of taking include or excude, we add them (include + exclude)

# Main code:
# if arr[i-1] <= j:
#   table[i][j] = table[i-1][j] + table[i-1][j-arr[i-1]]
# else:
#   table[i][j] = table[i-1][j]


# Recursive method
def func(arr, val, n):
    if val == 0:
        return 1
    if n == 0:
        return 0
    
    if arr[n-1] <= val:
        return func(arr, val-arr[n-1], n-1) + func(arr, val, n-1)
    else:
        return func(arr, val, n-1)

arr = [2, 3, 7, 8, 10]
val = 10
n = len(arr)
print(func(arr, val, n))


# Memoization method
table = [[0 for j in range(val+1)] for i in range(n+1)]
def func(arr, sum, n):
    if sum == 0:
        return 1
    if n == 0:
        return 0
    
    if table[n][sum] != 0:
        return table[n][sum]
    elif arr[n-1] <= sum:
        table[n][sum] = func(arr, sum-arr[n-1], n-1) + func(arr, sum, n-1)
        return table[n][sum]
    else:
        table[n][sum] = func(arr, sum, n-1)
        return table[n][sum]


# Top-dowm approach
print(func(arr, val, n))
def func(arr, sumval, n):
    table = [[0 for j in range(sumval+1)] for i in range(n+1)]
        
    for i in range(n+1):
        table[i][0] = 1
    for j in range(1, sumval+1):
        table[0][j] = 0
    
    for i in range(1, n+1):
        for j in range(1, sumval+1):
            if arr[i-1] <= j:
                table[i][j] = table[i-1][j-arr[i-1]] +  table[i-1][j]
            else:
                table[i][j] = table[i-1][j]

    return table[n][sumval]
print(func(arr, val, n))
