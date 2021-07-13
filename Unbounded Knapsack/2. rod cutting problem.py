# Given a rod of length l, length array and prices at that length array. we've to cut
# the rod such that the profit is maximum

# length = [1, 2, 3, 4, 5, 6, 7, 8]
# price = [1, 5, 8, 9, 10, 17, 17, 20]
# l = 8

# we can cut this rod into rod of length 1 and 7 -> profit = 1 + 17
# rod of length (2, 6) -> profit = 5 + 17
# rod of length (2, 3, 3) -> profit = 5 + 8 + 8
# rod of length (1, 2, 5) -> profit = 1 + 5 + 10
# and many more combinations. cut the rod in such way that profit is maximum

# Note: this is exactly 0/1 knapsack problem with multible occurence of items
# Similarity btw 0/1 and knapsack:
# weight array --> length array
# value array --> price array 
# W (weight constraint) --> l (length of rod)


# Solution is similar to unbounded standard problem

# Recursive solution
def rodCut(length, price, l, n):
    if n == 0 or l == 0:
        return 0
    
    if length[n-1] <= l:
        return max(price[n-1] + rodCut(length, price, l-length[n-1], n), rodCut(length, price, l, n-1))
    else:
        return rodCut(length, price, l, n-1)

length = [1, 2, 3, 4, 5, 6, 7, 8]
price = [1, 5, 8, 9, 10, 17, 17, 20]
l = 8
n = len(price)
print(rodCut(length, price, l, n))


# Memoization method
table = [[-1 for j in range(l+1)] for i in range(n+1)]
def rodCut(length, price, l, n):
    if l == 0 or n == 0:
        return 0
    if table[n][l] != -1:
        return table[n][l]
    
    if length[n-1] <= l:
        table[n][l] = max(price[n-1] + rodCut(length, price, l-length[n-1], n), rodCut(length, price, l, n-1))
        return table[n][l]
    else:
        table[n][l] = rodCut(length, price, l, n-1)
        return table[n][l]

print(rodCut(length, price, l, n))


# Top-Down approach
def rodCut(length, price, l, n):
    table = [[0 for j in range(l+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(l+1):
            if i == 0 or j == 0:
                table[i][j] = 0
            if length[i-1] <= j:
                table[i][j] = max(price[i-1] + table[i][j-length[i-1]], table[i-1][j])
            else:
                table[i][j] = table[i-1][j]
    return table[n][l]

print(rodCut(length, price, l, n))