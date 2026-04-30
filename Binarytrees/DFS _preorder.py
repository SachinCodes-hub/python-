# Traversal - DFS - PREORDER (root - left - right)


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None 
        self.left = None
    

five = Node("5")
three = Node("3")
two  = Node("2")
nine = Node("9")
four = Node("4")
eight = Node("8")
one = Node("1")
six = Node("6")
ten = Node("10")


five.left = three
five.right = four

three.left = two
three.right = nine

four.left = eight
four.right = ten

eight.left = one
eight.right = six

print(five.left.right.val)


print(five.right.left.val)


#binary tree created 



# traversal methods


# 1. preorder - root left right

def preorder(node):
    if node ==None: # when no node left to traverse return(stop) not value . 
        return 
    print(node.val)
    
    preorder(node.left)
    preorder(node.right)
    

preorder(five)





#inorder traversal - left - root - right


def inorder(node):
    if node == None:
        return 
    
    inorder(node.left)
    print(node.val)
    inorder(node.right)
    


inorder(five)

# post order traversal  - [left right root]

def postorder(node):
    if node == None: # node should ot be any left dosent matter the value
        return
    print(node.val)
    
    postorder(node.left)
    postorder(node.right)
    

postorder(five)
    

