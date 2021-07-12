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


# Memoization method: 
# 1. To memoize, we just need to add few lines of code in recursive solution

# 2. variables which are changing in recursive code, i.e W and n. So we will create a
#    global matrix for these variables. Matrix of dimension (n+1) X (W+1)
# 3. Initialise this matrix with -1. Then store the values in matrix by recursion. 
# 4. IF value at perticular row, column is not -1, then we use that value. 
# 5. IF it is -1, then we call recursive call

wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]
W = 7
n = len(wt)

# Create matrix to store the values
table = [[-1 for j in range(W+1)] for i in range(n+1)]

def knapsack(wt, val, W, n):
    # Base condition
    if n == 0 or W == 0:
        return 0
    
    if table[n][W] != -1:
        return table[n][W]

    # Fill the table
    if wt[n-1] <= W:
        table[n][W] = max(val[n-1] + knapsack(wt, val, W-wt[n-1], n-1), knapsack(wt, val, W, n-1))
        return table[n][W]
    else:
        table[n][W] = knapsack(wt, val, W, n-1)
        return table[n][W]


print(knapsack(wt, val, W, n))

