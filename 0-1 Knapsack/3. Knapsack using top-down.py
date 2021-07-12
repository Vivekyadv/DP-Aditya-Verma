# Given weight and values of items, put these items in knapsack of capacity W to get
# maximum profit, max total value in knapsack

# Base condition: Think of smallest valid input
# when there is no item or when knapsack capacity is 0, max profit is 0.
# so, if n == 0 or W == 0:
#         return 0

# Choice diagram:
#              item weight w1
#             /              \
#         w1 <= W            w1 > We
#         /       \                \
#   select it   reject it        reject it

# Note: We always starts with the last item of given arrays


# Instead of recursive call, we make matrix of dimension (n+1) X (W+1). 
# These are two steps to make this matrix
# 1. Initialization
# 2. change recursive call into iterative method 

def knapsack(wt, val, W, n):
    table = [[0 for j in range(W+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(W+1):

            # Base condition
            if i == 0 or j == 0:
                table[i][j] = 0

            # Fill the table
            elif wt[i-1] <= j:
                table[i][j] = max(val[i-1] + table[i-1][j-wt[i-1]], table[i-1][j])
            else:
                table[i][j] = table[i-1][j]

    return table[n][W]

wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]
W = 7
n = len(wt)
print(knapsack(wt, val, W, n))