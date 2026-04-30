# find the maximum depth of a binary tree [height]
from collections import deque
#depth node take the value from children node to parent node only the max value out of both and increment on the next above node .. 

#rescusive


#root = Node
def solve(node):
    if node == None:
        return 0 #at the end node there will be no children nodes so thats why return 0 .
    leftHeight = solve(node.left)
    rightHeight = solve(node.right)
    return 1 + max(leftHeight ,rightHeight)


#solve(root)


# iterative solution - level order

def levelorder(root):
    queue = deque([])
    height =0 
    queue.append(root)
    while len(queue) != 0 :
        level_size = len(queue)
        height +=1
        for _ in range(level_size):
            e = queue.popleft()
            if e.left is not None:
                queue.append(e.left)
            if e.right is not None:
                queue.append(e.right)
    return height


