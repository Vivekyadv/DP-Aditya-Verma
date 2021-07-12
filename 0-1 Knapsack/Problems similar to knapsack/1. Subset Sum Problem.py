# Given array of integers and a sum value. Determine if there is a subset of the given
# array with sum = value


# Method 1: using recursion
def isSubsetSum(arr, val, n):

    # Base condition
    if val == 0:
        return True
    if n == 0:
        return False
    
    # Choice Diagram
    if arr[n-1] <= val:
        return isSubsetSum(arr, val-arr[n-1], n-1) or isSubsetSum(arr, val, n-1)
    else:
        return isSubsetSum(arr, val, n-1)
    
arr = [2, 3, 7, 8, 10]
val = 11
n = len(arr)
print(isSubsetSum(arr, val, n))


# Method 2: using memoization
# Create table first
table = [[-1 for j in range(val+1)] for i in range(n+1)]

def isSubsetSum(arr, val, n):
    # Base condition
    if val == 0:
        return True
    if n == 0:
        return False
    
    if table[n][val] != -1:
        return table[n][val]

    # Choice Diagram
    if arr[n-1] <= val:
        table[n][val] = isSubsetSum(arr, val-arr[n-1], n-1) or isSubsetSum(arr, val, n-1)
        return table[n][val]
    else:
        table[n][val] = isSubsetSum(arr, val, n-1)
        return table[n][val]

print(isSubsetSum(arr, val, n))


# Method 3: top-down method
def isSubsetSum(arr, val, n):
    # Initialise the table
    table = [[0 for j in range(val+1)] for i in range(n+1)]

    # Base condition
    for i in range(n+1):
        table[i][0] = True
    # We start this loop with 1 because table[0][0] = True
    for j in range(1, val+1):
        table[0][j] = False
    
    # Fill the table
    for i in range(1, n+1):
        for j in range(1, val+1):
            if arr[i-1] <= j:
                table[i][j] = table[i-1][j-arr[i-1]] or table[i-1][j]
            else:
                table[i][j] = table[i-1][j]

    return table[n][val]

print(isSubsetSum(arr, val, n))
