# Given a string, print the longest repeating subsequence such that the two subsequence 
# don't have same string character at same position, i.e., any i’th character in the two 
# subsequences shouldn’t have the same index in the original string.

# Example:      string = 'aabebcdd'     ans = 'abd',  len = 3

def func(string):
    n = len(string)
    table = [[0]*(n+1) for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if string[i-1] == string[j-1] and i != j:
                table[i][j] = 1 + table[i-1][j-1]
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    
    len_LRS = table[n][n]
    
    # print LRS
    i, j = n, n
    lrs = ''
    while i > 0 and j > 0:
        if string[i-1] == string[j-1] and i != j:
            lrs = string[i-1] + lrs
            i -= 1
            j -= 1
        else:
            if table[i][j-1] > table[i-1][j]:
                j -= 1
            else:
                i -= 1

    return lrs


string = 'aabebcdd'
print(func(string))


# Note: for string = 'axxxy' ans is xx
# first occurence xx -> (1,2)
# second occerence xx -> (2,3)
# x at index 0 in xx, 1 != 2
# x at index 1 in xx, 2 != 3 