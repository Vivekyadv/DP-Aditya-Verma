# Given a binary tree in which each node element contains a number. Find the maximum 
# possible sum from one leaf node to another.

#         -15
#        /   \
#       5     6
#      / \   / \
#    -8  1  3   9
#    / \         \ 
#   2   6         0
#                / \
#               4  -1
#                  /
#                 10

# In above tree, max path sum =  27  (3 + 6 + 9 + 0 – 1 + 10)

def solve(root, res):
    if root == None:
        return 0
    
    l = solve(root.left, res)
    r = solve(root.right, res)

    temp = max(l, r) + root.val
    if root.left == None and root.right == None:
        temp = max(temp, root.val)
    ans = max(temp, l + r + root.val)
    res[0] = max(res[0], ans)

    return temp

def main(root):
    res = [-2**32]
    temp = solve(root, res)
    return res[0]

