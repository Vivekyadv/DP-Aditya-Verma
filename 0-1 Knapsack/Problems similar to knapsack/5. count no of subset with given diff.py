# Given an array and a value x, partition it into two subsets such that difference of
# their sums is equal to x. we've to find no of such subsets pairs

# Example: arr = [1, 4, 2, 7, 3]  diff = 3
# subsets pair = [1, 4, 2] and [7, 3]
# [4, 3] and [7, 1, 2]
# [1, 4, 2, 3] and [7]

# so total no of such subsets pairs are 3

# Reduce it into problem which we already solve
# condition in this problem is s1 - s2 = diff, and we know that s1 + s2 = sum(arr)
# adding both equations -> 2*s1 = sum(arr) + diff
# so, s1 = (sum(arr) + diff)//2

# Now we have to count no of subsets with sum = s1
# This problem is now reduced to problem "count no of subset sum with given sum value"

def solve(arr, n, diff):
    x = (sum(arr) + diff)//2
    table = [[0 for j in range(x+1)] for i in range(n+1)]
    
    for i in range(n+1):
        table[i][0] = 1
    for j in range(1, x+1):
        table[0][j] = 0
    
    for i in range(1, n+1):
        for j in range(1, x+1):
            if arr[i-1] <= j:
                table[i][j] = table[i-1][j] + table[i-1][j-arr[i-1]]
            else:
                table[i][j] = table[i-1][j]
    
    return table[n][x]

arr = [1, 4, 2, 7, 3]
n = len(arr)
diff = 3
print(solve(arr, n, diff))


# Note: instead of adding both equations, we can also subtract them.
# s1 - s2 = diff and s1 + s2 = sum(arr)    which given -> 2s2 = sum(arr) - diff
# so, s2 = (sum(arr) - diff)//2
# We have to take absolute value of this because x = (sum(arr) - diff)//2 can't be -ve