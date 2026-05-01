# floor the value in binary search tree - largest value which is smaller than value given 
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


def floor(root, x):
    ans = - 1
    temp = root
    
    while temp is not None:
        if temp.val <= x:
           ans = temp.val
           temp = temp.right
           
        else:
            temp = temp.left
        
    return ans



print(floor(nine , 6))