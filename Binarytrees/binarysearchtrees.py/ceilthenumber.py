# ceil the number find the number which is closer higher to teh given number - just higher to the given number . 

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    

nine = Node(9)
three = Node(3)
eleven = Node(11)
two = Node(2)
seven = Node(7)
ten = Node(10)
fifteen = Node(15)
four = Node(4)
eight = Node(8)
fourteen = Node(14)

nine.left = three
nine.right = eleven

three.left = two 
three.right = seven

seven.left = four
seven.right = eight

eleven.left = ten
eleven.right = fifteen 

fifteen.right = fourteen

"""
 while root - check while root is not none . 

if :

 root = val: 
 print(root.val)
 break
 
elif root.val < val:
root = root.right

else:
root = root.left

diff = root.val - val 
if diff == 1:
 print(root.val)

"""


# ceil the target
root = nine


# my solution 
target = 10
def ceil(target , root):
    while root is not None:
        if root.val == target:
           return root.val
           break
    
        elif(root.val < target):
            root = root.right
        
        else:
            root = root.left
        
        diff = root.val - target
        if diff == 1:
           print(root.val)
    
    
print(ceil(10 , nine))
        
        
 
 
 # actual solution
'''
target =13

ceil = -1

while root in not None:
    if root.val == target:
        return root.val
    
    elif root.val < target: # to ceil it properly
        root = root.right
    
    else:
        ceil = root.val
        root = root.left
        
    return ceil

'''
# TC - o(log2(N)) 
  