# Given array coins, you have to use these coins to make them equal to given sum value
# count no of possible ways you can make coins = sum value

# Example: coins = [1, 2, 3]
# 1 + 1 + 1 + 1 + 1
# 1 + 1 + 1 + 2
# 1 + 1 + 3                 count = 5 ways
# 1 + 2 + 2 
# 2 + 3


# This is similar to count subset sum in which we count no of possible subset 
# whose sum = given value

coins = [1, 2, 3]
Sum = 5
n = len(coins)

# Recursive method
def coinChange(coins, n, Sum):
    if Sum == 0:
        return 1
    if n == 0:
        return 0
    
    if coins[n-1] <= Sum:
        return coinChange(coins, n, Sum-coins[n-1]) + coinChange(coins, n-1, Sum)
    else:
        return coinChange(coins, n-1, Sum)

print(coinChange(coins, n, Sum))


# Memoization method
table = [[-1 for j in range(Sum+1)] for i in range(n+1)]
def coinChange(coins, n, Sum):
    if Sum == 0:
        return 1    
    if n == 0:
        return 0
    
    if coins[n-1] <= Sum:
        table[n][Sum] = coinChange(coins, n, Sum-coins[n-1]) + coinChange(coins, n-1, Sum)
        return table[n][Sum]
    else:
        table[n][Sum] = coinChange(coins, n-1, Sum)
        return table[n][Sum]

print(coinChange(coins, n, Sum))


# Top-down approach
def coinChange(coins, n, Sum):
    if Sum < 0:
        return 0
    table = []
    for i in range(n+1):
        table.append([1] + [0]*Sum)
    
    for i in range(1, n+1):
        for j in range(1, Sum+1):
            if coins[i-1] <= j:
                table[i][j] = table[i][j-coins[i-1]] + table[i-1][j]
            else:
                table[i][j] = table[i-1][j]
    return table[-1][-1]

print(coinChange(coins, n, Sum))


# Time and Space Complexity: O(n*Sum)

# Method 4: Space Complexity: O(n)
def coinChange(coins, n, Sum):
    if Sum < 0:
        return 0

    table = [1] + [0]*Sum
    for i in range(n):
        for j in range(coins[i], Sum+1):
            table[j] += table[j-coins[i]]

    return table[Sum]
    