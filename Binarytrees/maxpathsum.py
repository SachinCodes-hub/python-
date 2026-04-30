# maximum sum of the path 

maxi = float("-inf")

def solve(node):
    if node is None:
        return 0 
    leftsum = solve(node.left)
    if leftsum < 0 :
        leftsum = 0 
    
    rightsum = solve(node.right)
    
    if rightsum < 0 :
        rightsum =0 
        
    maxi = max(maxi , leftsum +node.val+rightsum)
    
    return node.val + max(leftsum , rightsum)

solve(root)

