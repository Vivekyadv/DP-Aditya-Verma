# Given array coins and sum value (X). Find min no of coins required to make sum = X
# If it is not possible then return -1

# Example: coins = [1, 2, 3]
# 1 + 1 + 1 + 1 + 1
# 1 + 1 + 1 + 2
# 1 + 1 + 3                 Minimum no of coins = 2 (2,3) to make 5
# 1 + 2 + 2 
# 2 + 3


# Method 1: Time and Space Complexity = O(n*Sum)
def minCoins(coins, n, Sum):
    INT_MAX = 2**32
    table = [[0 for j in range(Sum+1)] for i in range(n+1)]
    for j in range(Sum+1):
        table[0][j] = INT_MAX - 1
        if j % coins[0] == 0:
            table[1][j] = j//coins[0]
        else:
            table[1][j] = INT_MAX - 1
    
    for i in range(2, n+1):
        for j in range(1, Sum+1):
            if coins[i-1] <= j:
                table[i][j] = min(1 + table[i][j-coins[i-1]], table[i-1][j])
            else:
                table[i][j] = table[i-1][j]
    return -1 if table[n][Sum] == INT_MAX-1 else table[n][Sum]

coins = [3, 10, 2]
n = len(coins)
Sum = 7
print(minCoins(coins, n, Sum))



# Method 1: Space complexity = O(n)
def minCoins(coins, n, Sum):
    INT_MAX = 2**32
    table = [0] + [INT_MAX]*Sum

    for i in range(n):
        for j in range(1, Sum + 1):
            if coins[i] <= j:
                temp = table[j - coins[i]]
                if temp != INT_MAX and temp + 1 < table[j]:
                    table[j] = temp + 1

    return -1 if table[Sum] == INT_MAX else table[Sum]

print(minCoins(coins, n, Sum))
