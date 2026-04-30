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



# traversal

def preorder(node):
    if node ==None: # when no node left to traverse return(stop)
        return 
    print(node.val)
    
    preorder(node.left)
    preorder(node.right)
    

preorder(five)





#inorder traversal - left - root - right


def inorder(node):
    if node.val == None:
        return 
    
    print(node.val)
    inorder(node.left)
    inorder(node.right)
    


inorder(three)
    