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


# Recursive method
def knapsack(wt, val, W, n):
    # Base condition
    if n == 0 or W == 0:
        return 0
    
    # Choice diagram
    if wt[n-1] <= W:
        return max(val[n-1] + knapsack(wt, val, W-wt[n-1], n-1), knapsack(wt, val, W, n-1))
    else:
        return knapsack(wt, val, W, n-1)

wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]
W = 7
n = len(wt)
print(knapsack(wt, val, W, n))