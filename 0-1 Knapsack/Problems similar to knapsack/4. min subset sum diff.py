# Given a set of integers, the task is to divide it into two sets S1 and S2 such that 
# the absolute difference between their sums is minimum. 

# Example: [1, 6, 11, 5]        [1,5,6] and [11] -> 12-11 = 1 which is minimum


# Solution using Recursion
def func(arr, i, sumCalc, arrSum):
    if i == 0:
        return abs(arrSum - 2*sumCalc)
    return min(func(arr, i-1, sumCalc+arr[i-1], arrSum), func(arr, i-1, sumCalc, arrSum))

def minSumDiff(arr, n):
    arrSum = sum(arr)
    return func(arr, n, 0, arrSum)

arr = [1, 6, 11, 5]
n = len(arr)
print(minSumDiff(arr, n))



# Top-down method
def minSumDiff(arr, n):
    arrSum = sum(arr)
    x = arrSum//2
    table = [[0 for j in range(x+1)] for i in range(n+1)]
    for i in range(n+1):
        table[i][0] = 1
    for j in range(1, x+1):
        table[0][j] = 0
    
    for i in range(1, n+1):
        for j in range(1, x+1):
            if arr[i-1] <= j:
                table[i][j] = table[i-1][j] or table[i-1][j-arr[i-1]]
            else:
                table[i][j] = table[i-1][j]

    lastRow = []
    for j in range(x+1):
        if table[n][j] == 1:
            lastRow.append(j)

    minval = float('inf')
    for i in range(len(lastRow)):
        minval = min(minval, arrSum-2*lastRow[i])
    
    return minval

arr = [1, 6, 11, 5]
n = len(arr)
print(minSumDiff(arr, n))
