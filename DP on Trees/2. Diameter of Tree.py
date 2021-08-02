# Given binary tree, you need to calculate the length of diameter.
# Diameter - length of longest path between any two nodes in tree
#          1
#         / \
#        2   3      diameter = 3, path = [4,2,1,3] or [5,2,1,3]
#       / \     
#      4   5  


def solve(root, res):
    if root == None:
        return 0
    
    l = solve(root.left, res)
    r = solve(root.right, res)

    temp = 1 + max(l, r)
    ans = max(temp, 1+l+r)
    res[0] = max(res[0], ans)

    return temp

def main(root):
    res = [-2**32]
    variable = solve(root, res)
    return res[0]

# We use result as array instead of normal integer variable because in every function call
# l = solve(root.left, res) and r = solve(root.right, res), the result value changes. 
# That's why we use result as array. It's similar to pass by reference in C++
