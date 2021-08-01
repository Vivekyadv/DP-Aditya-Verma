# Given e eggs and f floors in building. Find the minimum number of attempts to find
# the critical floor with the given number of eggs in worst case. We can have leftover
# eggs. 

# Example: eggs = 2, floors = 4
# min number of attempts = 3


# Method 1: using recursion
def solve(e, f):
    if f == 0 or f == 1:
        return f
    if e == 1:
        return f

    minval = 2**32
    for k in range(1, f+1):
        temp = 1 + max(solve(e-1, k-1), solve(e, f-k))
        minval = min(minval, temp)

    return minval

f = 14
e = 2
print(solve(e, f)) 


# Method 2: memoization method
f = 36
e = 2
table = [[-1]*(f+1) for i in range(e+1)]
def solve(e, f):
    if f == 0 or f == 1:
        return f
    if e == 1:
        return f

    if table[e][f] != -1:
        return table[e][f]

    minval = 2**32
    for k in range(1, f+1):
        temp = 1 + max(solve(e-1, k-1), solve(e, f-k))
        minval = min(minval, temp)

    table[e][f] = minval
    return minval

print(solve(e, f))

# A little bit optimization can be done in above method (memoization method)
table = [[-1]*(f+1) for i in range(e+1)]
def solve(e, f):
    if f == 0 or f == 1:
        return f
    if e == 1:
        return f

    if table[e][f] != -1:
        return table[e][f]

    minval = 2**32
    for k in range(1, f+1):
        if table[e-1][k-1] != -1:
            egg_break = table[e-1][k-1]
        else:
            egg_break = solve(e-1, k-1)
            table[e-1][k-1] = egg_break
        
        if table[e][f-k] != -1:
            egg_not_break =  table[e][f-k]
        else:
            egg_not_break = solve(e, f-k) 
            table[e][f-k] = egg_not_break

        temp = 1 + max(egg_break, egg_not_break)
        minval = min(minval, temp)

    table[e][f] = minval
    return minval

print(solve(e, f))
