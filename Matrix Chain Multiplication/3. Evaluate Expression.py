# Given a boolean expression with symbols: T, F, &, | and ^
# Count the number of ways we can parenthesize the expression so that the value of 
# expression evaluates to True.
# 
# Example: "T ^ F & T"      count = 2
# method 1 =  (T ^ F) & T -> T & T = T
# method 2 =  T ^ (F & T) -> T ^ F = T


def solve(string, i, j, flag):
    if i > j:
        return 0
    if i == j:
        if flag:
            return 1 if string[i] == 'T' else 0
        else:
            return 1 if string[i] == 'F' else 0
    
    ans = 0
    for k in range(i+1, j, 2):
        lT = solve(string, i, k-1, True)
        lF = solve(string, i, k-1, False)
        rT = solve(string, k+1, j, True)
        rF = solve(string, k+1, j, False)

        if string[k] == '&':
            if flag:
                ans += lT*rT
            else:
                ans += lF*rT + lT*rF + lF*rF 
        elif string[k] == '|':
            if flag:
                ans += lT*rT + lT*rF + lF*rT
            else:
                ans += lF*rF
        elif string[k] == '^':
            if flag:
                ans += lF*rT + lT*rF
            else:
                ans += lT*rT + lF*rF
    
    return ans

string = 'T|T&F^T'
n = len(string)
flag = True
print(solve(string, 0, n-1, 1) % 1003)



# Method 2: Memoization method (bottom up DP)
# solve(string, i, j, flag) -> number of variables that keep changing = i, j, flag = 3
# so, we'll create 3D table. Take table of dimension -> table[n+1][n+1][2]

t = [[[-1 for k in range(2)] for j in range(n+1)] for i in range(n+1)]

def solve(string, i, j, flag):
    if i > j:
        return 0
    if i == j:
        if flag:
            return 1 if string[i] == 'T' else 0
        else:
            return 1 if string[i] == 'F' else 0

    if t[i][j][flag] != -1:
        return t[i][j][flag]
    
    ans = 0
    for k in range(i+1, j, 2):
        if t[i][k-1][1] != -1:
            lT = t[i][k-1][1]
        else:
            lT = solve(string, i, k-1, 1)

        if t[i][k-1][0] != -1:
            lF = t[i][k-1][0]
        else:
            lF = solve(string, i, k-1, 0)
        
        if t[k+1][j][1] != -1:
            rT = t[k+1][j][1]
        else:
            rT = solve(string, k+1, j, 1)

        if t[k+1][j][0] != -1:
            rF = t[k+1][j][0]
        else:
            rF = solve(string, k+1, j, 0)

        if string[k] == '&':
            if flag:
                ans += lT*rT
            else:
                ans += lT*rF + lF*rT + lF*rF
        
        elif string[k] == '|':
            if flag:
                ans += lT*rT + lT*rF + lF*rT
            else:
                ans += lF*rF

        elif string[k] == '^':
            if flag:
                ans += lT*rF + lF*rT 
            else:
                ans += lT*rT + lF*rF
        t[i][j][flag] = ans
        
    return ans

print(solve(string, 0, n-1, 1) % 1003)



# Method 3: instead of using matrix, we can use map (dictionary) to store the values
store = {}
def solve(string, i, j, flag):
    if i > j:
        return 0
    if i == j:
        if flag:
            return 1 if string[i] == 'T' else 0
        else:
            return 1 if string[i] == 'F' else 0
    
    tempStr = str(i) + ' ' + str(j) + ' ' + str(flag)
    if tempStr in store:
        return store[tempStr]

    ans = 0
    for k in range(i+1, j, 2):
        lT = solve(string, i, k-1, True)
        lF = solve(string, i, k-1, False)
        rT = solve(string, k+1, j, True)
        rF = solve(string, k+1, j, False)

        if string[k] == '&':
            if flag:
                ans += lT*rT
            else:
                ans += lF*rT + lT*rF + lF*rF 
        elif string[k] == '|':
            if flag:
                ans += lT*rT + lT*rF + lF*rT
            else:
                ans += lF*rF
        elif string[k] == '^':
            if flag:
                ans += lF*rT + lT*rF
            else:
                ans += lT*rT + lF*rF
    
    store[tempStr] = ans
    return ans

print(solve(string, 0, n-1, 1) % 1003)
