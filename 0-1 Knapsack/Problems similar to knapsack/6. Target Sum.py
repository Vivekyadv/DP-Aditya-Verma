



def solve(arr, n, target):
    total = sum(arr)
    if target > total or (target + total) % 2:
        return 0

    x = (total + target)//2
    table = [[0 for j in range(x+1)] for i in range(n+1)]
    
    for i in range(n+1):
        table[i][0] = 0
    for j in range(1, x+1):
        table[0][j] = 0
    table[0][0] = 1
    
    for i in range(1, n+1):
        for j in range(x+1):
            if arr[i-1] <= j:
                table[i][j] = table[i-1][j] + table[i-1][j-arr[i-1]]
            else:
                table[i][j] = table[i-1][j]
    
    return table[n][x]

arr = [1, 4, 2, 7, 3]
n = len(arr)
target = 3
print(solve(arr, n, target))
