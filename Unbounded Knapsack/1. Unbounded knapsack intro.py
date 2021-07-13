# Given weight and value arrays, weight constraint (W) max capacity of knapsack
# we need to maximise the profit. here we are allowed to use unlimited number of 
# instances of an item.


# How it is different from 0/1 Knapsack?
# In 0/1 knapsack, either we choose or not that item is processed. But in unbounded
# knapsack, if we do not choose item, it is processed and now we call func on remaining
# n-1 items. But if we choose the item, still we can choose again so we call func on
# n items. 


# Recursive solution
def knapsack(wt, val, W, n):
    # Base condition
    if n == 0 or W == 0:
        return 0
    
    # Choice diagram
    if wt[n-1] <= W:
        return max(val[n-1] + knapsack(wt, val, W-wt[n-1], n), knapsack(wt, val, W, n-1))
    else:
        return knapsack(wt, val, W, n-1)

wt = [1, 3, 4, 5]
val = [10, 40, 50, 70]
W = 8
n = len(wt)
print(knapsack(wt, val, W, n))


# Memoization method
table = [[-1 for j in range(W+1)] for i in range(n+1)]

def knapsack(wt, val, W, n):
    # Base condition
    if n == 0 or W == 0:
        return 0
    
    if table[n][W] != -1:
        return table[n][W]

    # Fill the table
    if wt[n-1] <= W:
        table[n][W] = max(val[n-1] + knapsack(wt, val, W-wt[n-1], n), knapsack(wt, val, W, n-1))
        return table[n][W]
    else:
        table[n][W] = knapsack(wt, val, W, n-1)
        return table[n][W]

print(knapsack(wt, val, W, n))



# Top-down approach
def knapsack(wt, val, W, n):
    table = [[0 for j in range(W+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(W+1):

            # Base condition
            if i == 0 or j == 0:
                table[i][j] = 0

            # Fill the table
            elif wt[i-1] <= j:
                table[i][j] = max(val[i-1] + table[i][j-wt[i-1]], table[i-1][j])
            else:
                table[i][j] = table[i-1][j]

    return table[n][W]


print(knapsack(wt, val, W, n))