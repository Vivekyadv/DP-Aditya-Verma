# Given an array of integers, determine whether this array can be partitioned into two
# subsets, such that the sum of elements in both subsets is the same. 

# Logic: if sum(arr) is odd, we can't partitioned it into two subsets as sum of both
# subsets should be equal.
# if sum(arr) is even then find if there is any subset with sum = sum(arr)//2

# Note: there is no need to find both subsets because if sum of one subset = sum(arr)//2
# then it is obvious that sum of other subset = sum(arr)//2

# So, now this problem reduced to previous one, subset sum problem.

# Using Recurssion
def isSubsetSum(arr, sumVal, n):
    # Base condition
    if sumVal == 0:
        return True
    if n == 0:
        return False
    
    # Choice Diagram
    if arr[n-1] <= sumVal:
        return isSubsetSum(arr, sumVal-arr[n-1], n-1) or isSubsetSum(arr, sumVal, n-1)
    else:
        return isSubsetSum(arr, sumVal, n-1)
    
def findPartition(arr, n):
    arrSum = 0
    for i in range(n):
        arrSum += arr[i]
    
    if arrSum % 2 == 1:
        return False
    else:
        return isSubsetSum(arr, arrSum//2, n)

arr = [1, 5, 6, 2, 4]
n = len(arr)
print(findPartition(arr, n))



# Using memoization method
val = sum(arr)//2
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



# Using top-down method
def findPartition(arr, n):
    sumVal = sum(arr)
    if sumVal % 2 == 1:
        return False
    
    sumVal = sumVal//2
    # Initialise the table
    table = [[0 for j in range(sumVal+1)] for i in range(n+1)]

    # Base condition
    for i in range(n+1):
        table[i][0] = True
    # We start this loop with 1 because table[0][0] = True
    for j in range(1, sumVal+1):
        table[0][j] = False
    
    # Fill the table
    for i in range(1, n+1):
        for j in range(1, sumVal+1):
            if arr[i-1] <= j:
                table[i][j] = table[i-1][j-arr[i-1]] or table[i-1][j]
            else:
                table[i][j] = table[i-1][j]

    return table[n][val]

arr = [1, 5, 6, 2, 4]
n = len(arr)
print(findPartition(arr, n))




# Reduce space complexity:
# Note: this method is not feasible for arrays with big sum
def findPartition(arr, n):
    sumVal = sum(arr)
    if sumVal % 2 == 1:
        return False
    
    sumVal = sumVal//2
    table = [0] * (sumVal+1)
    
    for i in range(n):
        for j in range(sumVal, arr[i]-1, -1):
            if table[j-arr[i]] or j == arr[i]:
                table[j] = True

    return table[sumVal]

arr = [1, 5, 6, 2, 4]
n = len(arr)
print(findPartition(arr, n))