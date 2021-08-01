# Given two strings A and B, we may represent string A as binary tree by partitioning it
# to two non-empty substrings recursively.

# A = "great"       great
#                   /   \
#                  gr   eat
#                  /\    / \
#                 g  r  e   at
#                           /\
#                          a  t

# To scramble the string, we may choose any non-leaf node and swap its two children. 
# In above example, we can swap children of "gr" (which is non-leaf node)

#           rgeat
#           /   \
#          rg   eat
#          /\    / \        We can say "rgeat" is scrambled string of "great"
#         r  g  e   at
#                   /\
#                  a  t

# Similarly after swaping children of "eat" or "at", we get "rgate" or "rgeta"
# both are scrambled of "great"
# Note: "great" is also scrambled of "great"

# Method 1: using recursion 
def solve(a, b):
    if a == b:
        return True
    if len(a) <= 1:
        return False
    
    n = len(a)
    scramble = False
    for i in range(1, n):
        cond1 = solve(a[:i], b[n-i:]) and solve(a[i:], b[:n-i])
        cond2 = solve(a[:i], b[:i]) and solve(a[i:], b[i:])
        
        if cond1 or cond2:
            scramble = True
            break

    return scramble

def main(a, b): 
    if len(a) != len(b):
        return False
    if len(a) == len(b) == 0:
        return True
    return solve(a,b)

a = 'great'
b = 'eatgr'
print(main(a, b))


# Method 2: memoization 
# we can use either matrix or map to store values. In this method we're gonna use map 
store = {}
def solve(a, b):
    if a == b:
        return True
    if len(a) <= 1:
        return False
    
    tempStr = a + " " + b
    if tempStr in store:
        return store[tempStr]

    n = len(a)
    scramble = False
    for i in range(1, n):
        cond1 = solve(a[:i], b[n-i:]) and solve(a[i:], b[:n-i])
        cond2 = solve(a[:i], b[:i]) and solve(a[i:], b[i:])
        
        if cond1 or cond2:
            scramble = True
            break

    store[tempStr] = scramble
    return scramble

def main(a, b): 
    if len(a) != len(b):
        return False
    if len(a) == len(b) == 0:
        return True
    return solve(a,b)

print(main(a, b))

