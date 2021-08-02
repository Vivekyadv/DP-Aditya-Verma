# In previous question, we have to find max length from leaf node to another leaf node.
# In this question, we can move from any node to any other node. We've to find maximum
# path sum.

#   -10
#   / \
#  9  20        ans = 15+20+7 = 42
#    /  \
#   15   7


def solve(root, res):
    if root == None:
        return 0
    
    l = solve(root.left, res)
    r = solve(root.right, res)

    temp = max(root.val + max(l, r), root.val)
    ans = max(temp, l + r + root.val)
    res[0] = max(ans, res[0])

    return temp

def main(root):
    res = [-2**32]
    temp = solve(root, res)
    return res[0]
