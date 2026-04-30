# Diameter of a binary tree - longest path of in the tree 

diameter = 0 
def solve(node):
    if node == None:
        return 0
    leftHeight = solve(node.left)
    rightHeight = solve(node.right)
    diameter = max(diameter , leftHeight + rightHeight)
    return 1 + max(leftHeight , rightHeight)


    return diameter