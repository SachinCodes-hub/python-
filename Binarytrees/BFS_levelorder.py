
#important line for deque importing 

from collections import deque # importing doubly queue

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
    
    
one = Node("1")

two  = Node("2")
three = Node("3")
four  = Node("4")
five = Node("5")
six  = Node("6")
seven = Node("7")



one.left = two 
one.right = three 
two.left = four 
two.right = five 

three.left = six 
three.right = seven

# BFS - level order traversal 

# time complexity - O(N) , space complexity - o(N)

def levelorder(node):
    result = []
    queue = deque({})
    queue.append(node)
    
    while len(queue) != 0 :
        e = queue.pop()
        result.append(e) # while getting the value of node - value , data , face 
        
        if e.left is not None:
            queue.append(e.left)
        
        if e.right is not None:
            queue.append(e.right)
    
    
    return result 
    

levelorder(one)
    
    