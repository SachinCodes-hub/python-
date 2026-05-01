# insert the given node at right position according to its value

"""
1.find the correct position of the node where should it be inserted
2. attach it 


"""

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

fifteen.left = fourteen



newnode = Node(17)

root = nine

temp = root

"""

# solution  - own
while True:
    
    if temp.val < newnode.val:
        if temp.right == None :
            temp.right = newnode
        
        temp = temp.right
        
    else:
        
        if temp.left == None:
            temp.left = newnode
        temp = temp.left
    
    
print(fifteen.right.val)

"""

# solutiom - optimal - 

temp = nine
while True :
    
    if temp.val > newnode.val:
        if temp.left is None:
            temp.left = newnode
            break
        temp = temp.left
    
    else :
        if temp.right is None:
            temp.right = newnode.val
            break
        temp = temp.right
    
print(fifteen.right)

print(newnode)


# time comlexity - o(log2(N))

# space complexity - O(log2(N))

