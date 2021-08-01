# Given dimensions of matrices in the form of array. Calculate the minimum cost of 
# multiplication of these matrices.

# Arr = [40, 20, 30, 10, 30]
# Dimensions -> A1 = 40 X 20,   A2 = 20 X 30,   A3 = 30 X 10,   A4 = 10 X 30
# Minimum cost -> 26000   
# (A1 x (A2 x A3)) x A4   =   8000 + 6000 + 12000 

# Explanation on Aditya Verma Video 
# Link: https://www.youtube.com/watch?v=kMK148J9qEE
# Playlist: https://www.youtube.com/watch?v=nqowUJzG-iM&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go 


# Recursive Method:
def solve(arr, i, j):
    if i >= j:
        return 0
    minval = 2**32
    for k in range(i, j):
        temp = solve(arr, i, k) + solve(arr, k+1, j) + arr[i-1]*arr[k]*arr[j]
        if temp < minval:
            minval = temp
    return minval

arr = [40, 20, 30, 10, 30]
n = len(arr)
print(solve(arr, 1, n-1))


# Memoization Method:
table = [[-1]*(n+1) for i in range(n+1)]
def solve(arr, i, j):
    if i >= j:
        return 0
    if table[i][j] != -1:
        return table[i][j]
    
    minval = 2**32
    for k in range(i, j):
        temp = solve(arr, i, k) + solve(arr, k+1, j) + arr[i-1]*arr[k]*arr[j]
        minval = min(minval, temp)
    table[i][j] = minval
    return table[i][j]

print(solve(arr, 1, n-1))
